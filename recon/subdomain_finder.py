#!/usr/bin/env python3
import requests

def find_subdomains(domain):
    wordlist = ['www', 'mail', 'ftp', 'cpanel', 'admin']
    found = []

    for sub in wordlist:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=2)
            if res.status_code < 400:
                print(f"[+] Found: {url}")
                found.append(url)
        except:
            pass
    return found

if __name__ == "__main__":
    domain = input("Enter domain: ")
    find_subdomains(domain)
    