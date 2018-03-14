import socket,json

# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("127.0.0.1", 6667) )

for i in range(0,2):
    # Kirim data ke server
    data = "Selamat sore"
    tcp_sock.send( data.encode('ascii') )

    # Baca dari server
    data = tcp_sock.recv(100)
    data = data.decode('ascii')
    print(data)

    #Tutup koneksi
    #tcp_sock.close()