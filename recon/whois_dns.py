#!/usr/bin/env python3
import socket
import whois

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] {domain} resolves to {ip}")
    except:
        print("[-] DNS lookup failed.")

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"[+] Registrar: {w.registrar}")
        print(f"[+] Creation Date: {w.creation_date}")
        print(f"[+] Expiry Date: {w.expiration_date}")
        print(f"[+] Emails: {w.emails}")
    except:
        print("[-] Whois failed.")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    dns_lookup(domain)
    whois_lookup(domain)
#     print("\n[+] Welcome to RedStrike Recon Module")