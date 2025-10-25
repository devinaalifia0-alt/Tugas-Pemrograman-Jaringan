import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 6000

def handle_client(conn, addr):
    data = conn.recv(1024).decode()
    print(f"[SERVER] Pelanggan {addr} mengambil {data}")
    # simulasi waktu pelayanan
    time.sleep(2)
    response = f"{data} telah dilayani oleh petugas."
    conn.sendall(response.encode())
    conn.close()
    print(f"[SERVER] {data} selesai dilayani.")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[SERVER] Multi-thread Server berjalan di {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
