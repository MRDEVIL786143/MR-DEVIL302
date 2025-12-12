import asyncio
import json
import time
import uuid
from typing import Dict

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Serve static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

SERVER_START = time.time()
TOTAL_SENT = 0
TASKS: Dict[str, dict] = {}
LOCK = asyncio.Lock()


async def safe_send(ws: WebSocket, data: dict):
    try:
        await ws.send_text(json.dumps(data))
    except:
        pass


async def send_monitor(ws: WebSocket):
    uptime = int(time.time() - SERVER_START)

    async with LOCK:
        total_sent = TOTAL_SENT

    active = len([t for t in TASKS.values() if t["running"]])

    await safe_send(ws, {
        "type": "monitor_data",
        "uptime": uptime,
        "activeTasks": active,
        "totalSent": total_sent
    })


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.websocket("/ws")
async def websocket_handler(ws: WebSocket):
    await ws.accept()
    await safe_send(ws, {"type": "log", "message": "CONNECTED to Python Backend"})
    await send_monitor(ws)

    try:
        while True:
            msg = await ws.receive_text()
            data = json.loads(msg)

            if data["type"] == "monitor":
                await send_monitor(ws)

            # Start task
            elif data["type"] == "start":
                task_id = str(uuid.uuid4())[:8]

                entry = {
                    "id": task_id,
                    "ws": ws,
                    "cookie": data["cookieContent"],
                    "message": data["messageContent"],
                    "delay": float(data["delay"]),
                    "thread": data["threadID"],
                    "haters": data["hatersName"],
                    "last": data["lastHereName"],
                    "running": True,
                    "sent": 0
                }

                TASKS[task_id] = entry

                asyncio.create_task(task_loop(entry))

                await safe_send(ws, {"type": "task_started", "taskId": task_id})
                await safe_send(ws, {"type": "log", "message": f"Task {task_id} started"})

            # Stop task
            elif data["type"] == "stop_by_id":
                tid = data["taskId"]

                if tid in TASKS:
                    TASKS[tid]["running"] = False
                    await safe_send(ws, {"type": "stopped", "taskId": tid})
                    await safe_send(ws, {"type": "log", "message": f"Task {tid} stopped"})
                else:
                    await safe_send(ws, {"type": "log", "message": f"No Task ID {tid}"})


    except WebSocketDisconnect:
        pass


async def task_loop(task):
    global TOTAL_SENT

    ws = task["ws"]

    while task["running"]:
        await asyncio.sleep(task["delay"])

        task["sent"] += 1

        async with LOCK:
            TOTAL_SENT += 1

        await safe_send(ws, {
            "type": "log",
            "message":
                f"Sent #{task['sent']} (Thread: {task['thread']}) — Haters: {task['haters']} Last: {task['last']}"
        })

        await send_monitor(ws)

    await safe_send(ws, {"type": "log", "message": f"Task {task['id']} finished"})
