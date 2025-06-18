#!/bin/bash

echo "🔧 RedStrike Installer - Starting Setup..."

# Optional: Update system (for Linux users)
# sudo apt update && sudo apt upgrade -y

echo "📦 Installing required Python dependencies..."
pip3 install -r requirements.txt

echo "🛠️ Making core/menu.py executable..."
chmod +x core/menu.py

echo "✅ RedStrike is now ready to use!"
echo "👉 Run it with: python3 core/menu.py"

echo "🚀 Enjoy using RedStrike!"