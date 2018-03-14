import socket, threading, signal

#inisiasi objek socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.bind(("127.0.0.1", 6667))
tcp_sock.listen(100)
print ("Press ctrl+c to exit ...")

def handle_thread(conn) :
    while True :
        try :
            #terima data dari client
            data = conn.recv(200)
            data = data.decode('ascii')
            print(data)
            data = "OK"
            conn.send(data.encode('ascii'))
        except(socket.error) :
            conn.close()
            print("Connection close ...")
            break

#terima koneksi
while True :
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        conn, client_addr = tcp_sock.accept()
        t = threading.Thread(target= handle_thread, args= (conn,))
        t.start()
    except KeyboardInterrupt:
        break
   