import socket

# Inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan koneksi ke server
tcp_sock.connect( ("localhost", 4999) )

# Kirim data ke server
print("================== HAHA ==================")

data = input("Masukkan Suhu = ")
data1 = input("Masukkan Kelembaban Mutlak = ")
data2 = input("Masukkan Nilai Uap Air = ")
#data3 = input("Masukkan Nilai V = ")
#data4 = input("Masukkan Volume Sampel = ") 

tcp_sock.send( data.encode('ascii') )  
tcp_sock.send( data1.encode('ascii') )
tcp_sock.send( data2.encode('ascii') )
#tcp_sock.send( data3.encode('ascii') )
#tcp_sock.send( data4.encode('ascii') )

# Baca dari server
data = tcp_sock.recv(1000)
data = data.decode('ascii')
print(data)

#Tutup koneksi  
tcp_sock.close()