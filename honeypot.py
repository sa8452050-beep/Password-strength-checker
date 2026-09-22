import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 8080
LOG_FILE = "honeypot_log.txt"

def log_attempt(ip, port, data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Connection from {ip}:{port} - Data: {data}\n"
    print(entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(entry)

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Honeypot listening on {HOST}:{PORT}")
    print("Waiting for connections... (Ctrl+C to stop)\n")

    try:
        while True:
            client, addr = server.accept()
            try:
                data = client.recv(1024).decode(errors="ignore")
            except Exception:
                data = ""
            log_attempt(addr[0], addr[1], data.strip() or "(no data)")
            banner = b"220 FTP Server Ready\r\n"
            client.send(banner)
            client.close()
    except KeyboardInterrupt:
        print("\nHoneypot stopped.")
    finally:
        server.close()

if __name__ == "__main__":
    start_honeypot()
