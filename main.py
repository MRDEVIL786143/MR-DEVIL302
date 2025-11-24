from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Health check
@app.route("/")
def home():
    return "🔥 Mr Devil Cookies Server is running ✅"

# Fetch cookies from website
@app.route("/cookies", methods=["GET"])
def get_cookies():
    url = request.args.get("url")
    if not url:
        return "Error: URL parameter missing"
    try:
        response = requests.get(url)
        cookies = response.cookies.get_dict()
        return f"Cookies from {url}: {cookies}"
    except Exception as e:
        return f"Error fetching cookies: {e}"

# Send message with cookies
@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.form
    cookies = data.get("cookies")
    message = data.get("message")
    
    if not cookies or not message:
        return "Error: Cookies or message missing"
    
    # Simulate sending message
    print("Cookies used:", cookies)
    print("Message sent:", message)
    
    return f"Message processed successfully ✅: {message}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
