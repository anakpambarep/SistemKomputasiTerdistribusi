#author : erdiansahlan@student.ub.ac.id

import socket, time, signal

#inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect(("127.0.0.1", 6667))

while True :
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        # Kirim data ke server
        data = "Suhu      : 24 drjt \nKelembapan: 15% \nKdr O2    : 70mg\n"
        tcp_sock.send( data.encode('ascii') )
        # Baca dari server
        data = tcp_sock.recv(100)
        data = data.decode('ascii')
        time.sleep(2)   
    except KeyboardInterrupt:
        break