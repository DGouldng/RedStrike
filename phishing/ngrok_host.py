#!/usr/bin/env python3
import os
import subprocess
import time
import shutil
import requests
import pyperclip  # optional; install with pip if needed

def start_tracker():
    print("[*] Launching Flask tracker...")
    subprocess.Popen(["python3", "phishing/tracker.py"])
    time.sleep(3)

def start_ngrok(port=5000):
    if shutil.which("ngrok") is None:
        print("[!] ngrok not found. Run ./install.sh or install it manually.")
        return

    print("[*] Starting ngrok tunnel...")
    subprocess.Popen(["ngrok", "http", str(port)])
    time.sleep(3)

    try:
        response = requests.get("http://127.0.0.1:4040/api/tunnels")
        data = response.json()
        public_url = data['tunnels'][0]['public_url']
        print(f"[+] Public URL: {public_url}")

        try:
            pyperclip.copy(public_url)
            print("[*] URL copied to clipboard.")
        except:
            print("[*] Could not copy to clipboard (pyperclip may be missing).")

    except Exception as e:
        print(f"[!] Failed to retrieve ngrok URL: {e}")

if __name__ == "__main__":
    start_tracker()
    start_ngrok()
