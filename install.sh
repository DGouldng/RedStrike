#!/bin/bash

echo "[*] Installing RedStrike dependencies..."

# Update & install base dependencies
sudo apt update && sudo apt install -y python3 python3-pip git

# Install Python packages
pip3 install flask requests python-whois pyautogui

echo "[+] All dependencies installed successfully."
echo "✅ RedStrike is now ready to use!"
echo "[+] 👉 You can now run RedStrike with: python3 core/menu.py"

echo "🚀 Enjoy using RedStrike!"