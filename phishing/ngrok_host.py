#!/usr/bin/env python3
import os
import subprocess
import time

def start_ngrok(port=5000):
    print("[*] Launching Flask server...")
    subprocess.Popen(["python3", "phishing/tracker.py"])
    time.sleep(2)

    print("[*] Starting ngrok tunnel...")
    os.system(f"./ngrok http {port}")

if __name__ == "__main__":
    start_ngrok()
