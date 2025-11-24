from flask import Flask, request

app = Flask(__name__)

# ============================
#  ⚠️ Yahan apni COOKIES daalo
# ============================
COOKIES = {
    "x-fb-connection": "YOUR_COOKIE_HERE",
    "session-id": "YOUR_SESSION_ID",
    "token": "YOUR_TOKEN"
}

# ============================
#  Home Page
# ============================
@app.route("/")
def home():
    return """
    <h1>Mr Devil Cookies Server</h1>
    <p>Status: Running ✅</p>
    <p>POST request bhej kar message bhejo:</p>
    <ul>
        <li>/send?msg=HELLO</li>
    </ul>
    """


# ============================
#  Message Sender Endpoint
# ============================
@app.route("/send", methods=["GET"])
def send_message():
    msg = request.args.get("msg")

    if not msg:
        return {"error": "Message missing! /send?msg=HELLO"}, 400

    return {
        "status": "Message Sent Successfully ✔️",
        "your_message": msg,
        "cookies_attached": COOKIES
    }


# ============================
#  RUN SERVER
# ============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
