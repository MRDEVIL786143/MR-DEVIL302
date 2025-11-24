from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Example cookie fetching function
def fetch_cookies(url):
    try:
        response = requests.get(url)
        cookies = response.cookies.get_dict()
        return cookies
    except Exception as e:
        return {"error": str(e)}

# Route for fetching cookies
@app.route("/cookies", methods=["GET"])
def get_cookies():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter missing"}), 400

    cookies = fetch_cookies(url)
    return jsonify({"cookies": cookies})

# Health check route
@app.route("/")
def home():
    return "Mr Devil Cookies Server is running ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port)
