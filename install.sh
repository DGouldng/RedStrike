#!/bin/bash

function spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while ps -p $pid > /dev/null 2>&1; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
}

echo "🚀 Starting RedStrike Installation..."
sleep 1

echo "[1/4] 📦 Updating system packages... (ETA: 10s)"
(sudo apt update -y > /dev/null 2>&1) &
spinner
echo "✅ System updated."

echo "[2/4] 🔧 Installing base tools (python3, pip3, git)... (ETA: 10s)"
(sudo apt install -y python3 python3-pip git > /dev/null 2>&1) &
spinner
echo "✅ Tools installed."

echo "[3/4] 🐍 Installing Python dependencies (Flask, Requests, PyAutoGUI, WHOIS)... (ETA: 15s)"
(pip3 install flask requests python-whois pyautogui > /dev/null 2>&1) &
spinner
echo "✅ Python packages installed."

echo "[4/4] 🧼 Finalizing setup..."
sleep 2
echo "✅ RedStrike is now ready to use!"

echo ""
echo "[+] Run the tool with:  python3 core/menu.py"
echo "⚠️  Use ethically and with authorization only!"
echo ""
echo "💀 Happy Hacking with RedStrike! ⚔️"
