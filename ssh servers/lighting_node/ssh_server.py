import socket
import threading
import datetime
import os

BIND_IP = os.getenv("lighting_IP", "")
BIND_PORT = int(os.getenv("NODE_PORT", "2222"))

SSH_BANNER = b"SSH-2.0-OpenSSH_7.4p1 Debian-9+deb9u7\r\n"

def handle_client(client_socket, addr):
    print(f"[{datetime.datetime.now()}] Accepted connection from {addr}")
    try:
        client_socket.send(SSH_BANNER)
        client_socket.recv(1024)
        client_socket.send(b"Access denied.\r\n")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Error handling client {addr}: {e}")
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(10)
    print(f"[*] Listening on {BIND_IP}:{BIND_PORT}")

    while True:
        client, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client, addr))
        client_handler.start()

if __name__ == "__main__":
    main()
