#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🐱‍👤 MR DEVIL SIMPLE OAUTH TOKEN MAKER
- Sirf apne Facebook account ke liye
- Termux / PC friendly
- Roman Urdu messages
"""

import requests
import webbrowser
import threading
import os
from flask import Flask, request, render_template_string
from urllib.parse import urlencode

# ---------------- CONFIG ----------------
APP_ID = input("Apna Facebook App ID darj karein: ").strip()
APP_SECRET = input("Apna Facebook App Secret darj karein: ").strip()
REDIRECT_URI = "http://localhost:5000/callback"
GRAPH_VERSION = "v19.0"
SCOPE = input("Scopes (comma-separated, misal: public_profile,email,pages_show_list): ").strip() or "public_profile,email"
PORT = 5000
# ----------------------------------------

app = Flask(__name__)
token_data = {"short_token": None}

HTML_OK = """
<h2>✅ Token mil gaya!</h2>
<p>Terminal mein token dekho.</p>
"""

HTML_ERROR = """
<h2>❌ Error hua</h2>
<p>{{msg}}</p>
"""

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return render_template_string(HTML_ERROR, msg="Code nahi mila")

    # Exchange code for short token
    url = f"https://graph.facebook.com/{GRAPH_VERSION}/oauth/access_token"
    params = {
        "client_id": APP_ID,
        "redirect_uri": REDIRECT_URI,
        "client_secret": APP_SECRET,
        "code": code
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        short_token = data.get("access_token")
        token_data["short_token"] = short_token

        print("\n================ MR DEVIL TOKEN =================")
        print("Short-Lived Token:\n")
        print(short_token)
        print("\nExpires in (seconds):", data.get("expires_in"))
        print("================================================\n")
        return HTML_OK
    except Exception as e:
        return render_template_string(HTML_ERROR, msg=str(e))

def start_flask():
    app.run(host="0.0.0.0", port=PORT, threaded=True)

def open_browser():
    auth_params = {
        "client_id": APP_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "response_type": "code"
    }
    url = f"https://www.facebook.com/{GRAPH_VERSION}/dialog/oauth?" + urlencode(auth_params)
    print("\n🔗 Browser open kar raha hoon. Agar nahi hua to URL manually kholen:\n")
    print(url + "\n")
    try:
        webbrowser.open(url)
    except:
        pass

if __name__ == "__main__":
    print("\n🐱‍👤 MR DEVIL SIMPLE OAUTH TOKEN MAKER\n")
    t = threading.Thread(target=start_flask, daemon=True)
    t.start()
    open_browser()
    print("\n➡️ Browser mein login karein aur redirect hone dein (http://localhost:5000/callback).")
    print("👉 Token console mein print hoga.\n")

    # Wait for token
    try:
        while token_data["short_token"] is None:
            pass
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        os._exit(0)

    print("\n🎉 Kaam mukammal! Token ko safe jagah par rakhein.\n")
