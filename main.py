from flask import Flask, redirect, request, jsonify
import requests
import os

app = Flask(__name__)

FB_APP_ID = os.getenv("FB_APP_ID")
FB_APP_SECRET = os.getenv("FB_APP_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI", "https://your-render-url.onrender.com/callback")

@app.route("/")
def home():
    return """
    <h1>🔥 MrDevil OAuth Token Maker 🔥</h1>
    <p>Start karne ke liye neeche click karo:</p>
    <a href="/login">Login with Facebook</a>
    """

@app.route("/login")
def login():
    fb_auth_url = (
        f"https://www.facebook.com/v19.0/dialog/oauth?"
        f"client_id={FB_APP_ID}&redirect_uri={REDIRECT_URI}"
        "&scope=public_profile,email,pages_show_list"
    )
    return redirect(fb_auth_url)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Error: No code returned from Facebook."

    token_url = (
        f"https://graph.facebook.com/v19.0/oauth/access_token?"
        f"client_id={FB_APP_ID}&redirect_uri={REDIRECT_URI}"
        f"&client_secret={FB_APP_SECRET}&code={code}"
    )

    response = requests.get(token_url).json()
    return jsonify({
        "message": "🔥 MrDevil Token Ready 🔥",
        "token_data": response
    })

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
