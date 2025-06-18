#!/usr/bin/env python3
import pyautogui
import datetime
import os

def take_screenshot():
    filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    filepath = os.path.join("postex", filename)
    image = pyautogui.screenshot()
    image.save(filepath)
    print(f"[+] Screenshot saved: {filepath}")

if __name__ == "__main__":
    take_screenshot()
    
# Make sure to have the pyautogui library installed: pip3 install pyautogui
