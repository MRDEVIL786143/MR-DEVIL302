#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🍪 SAFE COOKIES SERVER
Yeh server sirf cookies ko store / read karta hai
Facebook login bypass ya hacking nahi karta
Render / Termux par chal jata hai
"""

from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# JSON file for saving cookies
FILE = "cookies.json"

# Load cookies from file if exists
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        cookies_store = json.load(f)
else:
    cookies_store = {}

@app.route("/")
def home():
    return "🍪 Cookies Server Running Safely!"

# Add or update cookie
@app.route("/add", methods=["POST"])
def add_cookie():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    if not key or not value:
        return jsonify({"error": "key aur value zaroori hain"}), 400

    cookies_store[key] = value
    with open(FILE, "w") as f:
        json.dump(cookies_store, f, indent=4)

    return jsonify({"message": f"Cookie '{key}' save ho gayi!"})

# Get cookie
@app.route("/get/<key>", methods=["GET"])
def get_cookie(key):
    if key not in cookies_store:
        return jsonify({"error": "Cookie mojood nahi"}), 404
    return jsonify({key: cookies_store[key]})

# Get all cookies
@app.route("/all", methods=["GET"])
def all_cookies():
    return jsonify(cookies_store)

# Delete cookie
@app.route("/delete/<key>", methods=["DELETE"])
def delete_cookie(key):
    if key in cookies_store:
        del cookies_store[key]
        with open(FILE, "w") as f:
            json.dump(cookies_store, f, indent=4)
        return jsonify({"message": f"Cookie '{key}' delete ho gayi!"})
    return jsonify({"error": "Cookie mojood nahi"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
