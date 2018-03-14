import socket,threading

def handle_thread(conn):
    while True :
        try :
            # Terima data dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            # Kirim balik ke client
            conn.send( data.encode('ascii') )
            # Tutup koneksi            
        except (socket.error) :
            # Koneksi diputus client, keluar dari thread
            conn.close()
            print("Koneksi diputus client")
            #tcp_sock.close() #baru ditambah
            break

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ikat di IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )

# Listen ke permintaan koneksi
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi
    conn, client_addr = tcp_sock.accept()
    # Start thread baru
    t = threading.Thread(target=handle_thread, args=(conn,))
    t.start()