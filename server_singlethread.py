import socket
import time

HOST = '127.0.0.1'
PORT = 6001

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[SERVER] Single-thread Server berjalan di {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        data = conn.recv(1024).decode()
        print(f"[SERVER] Pelanggan {addr} mengambil {data}")
        # Simulasi waktu melayani antrian
        time.sleep(2)
        response = f"{data} telah dilayani oleh petugas tunggal."
        conn.sendall(response.encode())
        conn.close()
        print(f"[SERVER] {data} selesai dilayani.\n")

if __name__ == "__main__":
    main()
