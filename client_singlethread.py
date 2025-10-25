import socket
import threading

HOST = '127.0.0.1'
PORT = 6001

def kirim_antrian(nomor):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        pesan = f"Nomor Antrian ke-{nomor}"
        s.sendall(pesan.encode())
        data = s.recv(1024).decode()
        print(f"[CLIENT {nomor}] Balasan server: {data}")

def main():
    threads = []
    print("[CLIENT] Mengirim 10 antrian ke server secara bersamaan...\n")

    for i in range(1, 11):
        t = threading.Thread(target=kirim_antrian, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
