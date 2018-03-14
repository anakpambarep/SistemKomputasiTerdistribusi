import socket

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ikat di IP dan port tertentu
tcp_sock.bind( ("localhost", 4999) )

# Listen ke permintaan koneksi
tcp_sock.listen(1000)

#while True :
# Terima permintaan koneksi
conn, client_addr = tcp_sock.accept()
# Terima data dari client
data = conn.recv(1000)
data1 = conn.recv(1000)
data2 = conn.recv(1000)
#data3 = conn.recv(1000)
#data4 = conn.recv(1000)

data = data.decode('ascii')
data1 = data1.decode('ascii')
data2 = data2.decode('ascii')
#data3 = data3.decode('ascii')
#data4 = data4.decode('ascii')
    
data = "Fahrenheit = ", int(data)*9/5+32, "Reamur = ", 4/5*int(data), "Kelvin = ", int(data)+273, "Kelembaban = ",int(data1)/int(data2)*100 # "Kadar Oksigen = ", int(data3)*0.025*8*1000/int(data4)
data = str(data)
# Kirim balik ke client
conn.send(data.encode('ascii') )
# Tutup koneksi
conn.close()