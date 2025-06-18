
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

### ⚠️ Legal Disclaimer
This tool is designed for authorized security testing, education, and learning.
Do not use RedStrike against systems without explicit permission.

The author is not responsible for any misuse or illegal activity.

### 🧠 Credits
Crafted by DGould – Follow for more offensive security and red teaming tools.
