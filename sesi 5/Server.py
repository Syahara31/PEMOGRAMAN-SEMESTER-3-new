import socket
import threading

# Menyimpan daftar koneksi client
clients = []

# Fungsi untuk mengirim pesan ke semua client lain
def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(message)
            except:
                # Jika client bermasalah, hapus dari daftar
                client.close()
                if client in clients:
                    clients.remove(client)

# Fungsi untuk menangani client individual
def handle_client(conn, addr):
    print(f"[TERHUBUNG] Client baru dari {addr}")
    conn.send("Selamat datang di server chat!\n".encode('utf-8'))

    while True:
        try:
            message = conn.recv(1024)
            if not message:
                break  # Jika tidak ada pesan, berarti client keluar

            print(f"[{addr}] {message.decode('utf-8')}")
            broadcast(message, conn)
        except:
            # Jika ada error koneksi
            print(f"[ERROR] Koneksi terputus dengan {addr}")
            break

    # Jika client keluar atau error
    conn.close()
    if conn in clients:
        clients.remove(conn)
    print(f"[PUTUS] {addr} terputus. Total client: {len(clients)}")

# Fungsi utama server
def main():
    host = '127.0.0.1'  # alamat lokal
    port = 55555        # port server

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"[MENUNGGU KONEKSI] Server berjalan di {host}:{port}")

    while True:
        try:
            conn, addr = server.accept()
            clients.append(conn)

            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

            print(f"[KLIEN TERHUBUNG] Total client aktif: {len(clients)}")
        except KeyboardInterrupt:
            print("\n[SERVER DIMATIKAN]")
            break
        except Exception as e:
            print(f"[KESALAHAN SERVER] {e}")

    # Tutup semua koneksi ketika server berhenti
    for client in clients:
        client.close()
    server.close()

if __name__ == "__main__":
    main()
