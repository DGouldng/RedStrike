#!/usr/bin/env python3

import os
import subprocess
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_banner():
    clear_screen()
    print("\033[93m")  # Start gold
    print(r""" 
██   ██  █████   ██████ ██   ██ ██████   ██████   ██████  ██    ██ ██      ██████  
██   ██ ██   ██ ██      ██  ██  ██   ██ ██       ██    ██ ██    ██ ██      ██   ██ 
███████ ███████ ██      █████   ██   ██ ██   ███ ██    ██ ██    ██ ██      ██   ██ 
██   ██ ██   ██ ██      ██  ██  ██   ██ ██    ██ ██    ██ ██    ██ ██      ██   ██ 
██   ██ ██   ██  ██████ ██   ██ ██████   ██████   ██████   ██████  ███████ ██████  

                    🔻REDSTRIKE | Red Team Toolkit
[+] Welcome to RedStrike - A Modular Penetration Testing Framework
[+] Developed by: DGould
[+] Version: 1.0
[+] Use responsibly and ethically!
""")
    print("\033[0m")  # Reset color

def run_script(path):
    print(f"\n[+] Running: {path}\n")
    try:
        subprocess.run(["python3", path], check=True)
    except Exception as e:
        print(f"[!] Error running {path}: {e}")
    input("\n[Press Enter to return to menu...]")  # This prevents instant clear


def view_logs(filepath):
    try:
        with open(filepath, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("[!] Log file not found.")
    input("\n[Press Enter to return to menu]")

def recon_menu():
    while True:
        show_banner()
        print("== RECON TOOLS ==")
        print("1. IP Tracker")
        print("2. Subdomain Finder")
        print("3. Port Scanner")
        print("4. WHOIS + DNS Lookup")
        print("0. Back\n")

        choice = input("Select option: ")

        if choice == "1":
            run_script("recon/ip_tracker.py")
        elif choice == "2":
            run_script("recon/subdomain_finder.py")
        elif choice == "3":
            run_script("recon/port_scanner.py")
        elif choice == "4":
            run_script("recon/whois_dns.py")
        elif choice == "0":
            break
        else:
            print("[!] Invalid choice")

def phishing_menu():
    while True:
        show_banner()
        print("== PHISHING TOOLS ==")
        print("1. Launch Tracker (Ngrok + Flask)")
        print("2. View Visitor Logs")
        print("0. Back\n")

        choice = input("Select option: ")

        if choice == "1":
            run_script("phishing/ngrok_host.py")
        elif choice == "2":
            view_logs("phishing/visitors.log")
        elif choice == "0":
            break
        else:
            print("[!] Invalid choice")

def postex_menu():
    while True:
        show_banner()
        print("== POST-EXPLOITATION TOOLS ==")
        print("1. Reverse Shell")
        print("2. Screenshot Capture")
        print("3. File Exfiltration")
        print("0. Back\n")

        choice = input("Select option: ")

        if choice == "1":
            run_script("postex/reverse_shell.py")
        elif choice == "2":
            run_script("postex/screenshot.py")
        elif choice == "3":
            run_script("postex/file_exfil.py")
        elif choice == "0":
            break
        else:
            print("[!] Invalid choice")

def c2_menu():
    while True:
        show_banner()
        print("== C2 COMMAND & CONTROL ==")
        print("1. Start C2 Server")
        print("2. Launch Agent (connect to C2)")
        print("0. Back\n")

        choice = input("Select option: ")

        if choice == "1":
            run_script("c2/c2_server.py")
        elif choice == "2":
            run_script("c2/agent.py")
        elif choice == "0":
            break
        else:
            print("[!] Invalid choice")

def list_modules(path):
    modules = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            if "index.html" in os.listdir(full_path) and "login.php" in os.listdir(full_path):
                modules.append((item, full_path, 'php'))
            elif any(f.endswith(".py") for f in os.listdir(full_path)):
                modules.append((item, full_path, 'python'))
    return modules

def run_module(name, path, mode):
    print(f"\n[+] Launching {name}...")
    if mode == 'php':
        subprocess.run(["php", "-S", "127.0.0.1:8080", "-t", path])
    elif mode == 'python':
        for file in os.listdir(path):
            if file.endswith(".py"):
                subprocess.run(["python3", os.path.join(path, file)])
                break

def dynamic_menu(section_name, folder):
    path = os.path.join(BASE_PATH, folder)
    modules = list_modules(path)
    if not modules:
        print(f"\n[!] No modules found in {folder}/")
        return

    while True:
        clear_screen()
        print(f"[ {section_name.upper()} MODULES ]\n")
        for i, (name, _, _) in enumerate(modules, start=1):
            print(f"{i}. {name}")
        print(f"{len(modules)+1}. Back to Main Menu\n")

        choice = input("Select > ")
        try:
            choice = int(choice)
            if choice == len(modules) + 1:
                break
            elif 1 <= choice <= len(modules):
                run_module(*modules[choice - 1])
        except:
            print("Invalid input.")
        input("\nPress Enter to return...")

def main_menu():
    while True:
        show_banner()
        print("== MAIN MENU ==")
        print("1. Recon Tools")
        print("2. Phishing Tools")
        print("3. Post-Exploitation")
        print("4. C2 & Payloads")
        print("q. Exit\n")

        choice = input("Select option: ")

        if choice == "1":
            recon_menu()
        elif choice == "2":
            phishing_menu()
        elif choice == "3":
            postex_menu()
        elif choice == "4":
            c2_menu()
        elif choice.lower() == "q":
            print("\n[!] Exiting RedStrike. Goodbye!\n")
            sys.exit()
        else:
            print("[!] Invalid choice")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n[!] Interrupted. Exiting RedStrike.")
        sys.exit()

# End of file