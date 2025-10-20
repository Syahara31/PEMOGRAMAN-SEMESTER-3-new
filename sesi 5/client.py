import socket
import threading

# Fungsi untuk menerima pesan dari server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Jika pesan kosong → koneksi terputus
                print("[SERVER TERPUTUS]")
                break
            print(message)
        except:
            print("[KESALAHAN] Koneksi ke server terputus.")
            client_socket.close()
            break

# Fungsi untuk mengirim pesan ke server
def send_messages(client_socket):
    while True:
        try:
            message = input('')
            if message.lower() == 'keluar':
                print("[INFO] Menutup koneksi...")
                client_socket.close()
                break
            client_socket.send(message.encode('utf-8'))
        except:
            print("[KESALAHAN] Gagal mengirim pesan. Koneksi terputus.")
            client_socket.close()
            break

def main():
    host = '127.0.0.1'  # alamat server
    port = 55555        # port server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
        print(f"[TERHUBUNG] Berhasil terhubung ke server {host}:{port}")
    except:
        print("[KESALAHAN] Tidak dapat terhubung ke server.")
        return

    # Jalankan dua thread secara paralel:
    # satu untuk menerima pesan, satu untuk mengirim
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    main()
