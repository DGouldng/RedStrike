#!/bin/bash
echo "🔧 Installing dependencies for RedStrike..."

sudo apt update
sudo apt install -y python3 python3-pip net-tools xclip

echo "📦 Installing Python libraries..."
pip3 install -r requirements.txt

echo "✅ Setup complete! Run with: python3 core/menu.py"

echo "🚀 Enjoy using RedStrike!"