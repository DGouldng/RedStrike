
# RedStrike ⚔️💀

A **modular Red Team offensive toolkit** for penetration testing and adversary simulation.  
Created by **DGould** — for **educational and ethical use only**.

---

## 🧩 Features & Modules

### 🕵️ Recon
- IP Tracker
- Subdomain Finder
- Port Scanner
- WHOIS + DNS Lookup

### 🎯 Phishing
- Ngrok Tracker (Flask server)
- JavaScript Stealer Page
- Visitor Logger (stores logs in `phishing/visitors.log`)

### 🎮 Post-Exploitation
- Reverse Shell Launcher
- Screenshot Capture
- File Exfiltration

### 🛰️ C2 - Command & Control
- C2 Server
- Agent to connect and receive tasks

---

## 💾 Installation

### ✅ Requirements
- Python 3.6+
- Git
- Unix/Linux or WSL/Parrot OS/Kali (for full compatibility)

### 🛠️ Steps

```bash
git clone https://github.com/DGouldng/RedStrike.git
cd RedStrike
chmod +x install.sh
./install.sh

```
### If needed manually:
```
pip install flask requests python-whois

```
### 🚀 Usage
```bash
python3 core/menu.py
```
### Navigate the menu to launch modules in:

Recon

Phishing

Post-Exploitation

C2 Server & Agents

### Hints

Telegram bot token is required for phishing/tracker.py modules

### 📩 Telegram Setup for tracker.py
1. Create a bot using @BotFather → get your bot token.
2. Get your Chat ID from @userinfobot.
3. In phishing/tracker.py, replace:
``` bash
    python
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

```
4. Save and run: 
```bash
python3 phishing/tracker.py
```

⚠️ This module uses ipinfo.io. Get a free token from https://ipinfo.io/signup and replace it in tracker.py.
#### 🔐 Keep your token and chat ID secret.

### **Conclusion**: 
This set up will send the visitor's credential to the telegram info provided. This is a basic example and can be modified to suit your needs. Please be aware that this is is for educational purposes only. Do not use this for malicious activities.

### ⚠️ Legal Disclaimer
This tool is designed for authorized security testing, education, and learning.
Do not use RedStrike against systems without explicit permission.

The author is not responsible for any misuse or illegal activity.

### 🧠 Credits
Crafted by DGould – Follow for more offensive security and red teaming tools.
