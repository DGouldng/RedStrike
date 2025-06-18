#!/usr/bin/env python3
import socket

def scan_ports(ip, ports=[21, 22, 23, 80, 443, 8080]):
    print(f"\n[*] Scanning {ip}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()

if __name__ == "__main__":
    ip = input("Enter target IP: ")
    scan_ports(ip)
