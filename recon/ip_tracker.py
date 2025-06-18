#!/usr/bin/env python3
import requests

def track_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        res = requests.get(url).json()

        if res['status'] == 'success':
            print(f"\n[+] IP: {res['query']}")
            print(f"[+] Country: {res['country']}")
            print(f"[+] Region: {res['regionName']}")
            print(f"[+] City: {res['city']}")
            print(f"[+] ISP: {res['isp']}")
            print(f"[+] Lat, Long: {res['lat']}, {res['lon']}")
        else:
            print("[-] Failed to fetch IP info")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    track_ip(ip)
