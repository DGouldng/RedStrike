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
(sudo apt install -y python3 python3-pip git unzip wget > /dev/null 2>&1) &
spinner
echo "✅ Base tools installed."

echo "[3/4] 🐍 Installing Python dependencies (Flask, Requests, PyAutoGUI, WHOIS)... (ETA: 15s)"
(pip3 install flask requests python-whois pyautogui > /dev/null 2>&1) &
spinner
echo "✅ Python packages installed."

echo "[4/4] 🌐 Checking ngrok installation..."
if ! command -v ngrok &> /dev/null
then
    echo "[*] ngrok not found. Installing ngrok..."
    wget -q https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
    unzip -q ngrok-stable-linux-amd64.zip
    sudo mv ngrok /usr/local/bin
    rm ngrok-stable-linux-amd64.zip
    echo "✅ ngrok installed successfully."
else
    echo "✅ ngrok already installed."
fi

echo ""
echo "🎯 Finalizing setup..."
sleep 2
echo "✅ RedStrike is now ready to use!"

echo ""
echo "📂 Navigate to project root and run:"
echo "   👉 \033[1mpython3 core/menu.py\033[0m"
echo ""
echo "⚠️  Use responsibly and ethically. Only with authorized permission."
echo "💀 Happy Hacking with RedStrike! ⚔️"
echo "Lunching RedStrike in 3 seconds..."
sleep 3
python3 core/menu.py