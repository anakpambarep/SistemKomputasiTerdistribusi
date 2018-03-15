#author : erdiansahlan@student.ub.ac.id

#import library http client
import http.client
import json

ip_server = "127.0.0.1"
port_server = 7777

# kirim request get dengan url /mahasiswa
# Inisiasi koneksi ke server
conn = http.client.HTTPConnection(ip_server,port=port_server)
conn.request('GET','/mahasiswa')

# Baca response nya
response = conn.getresponse().read()

def tambah_mahasiswa():
    # kirim request get dengan url /mahasiswa
    # Inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # definisikan headernya
    header = {"Content-Type" : "application/json"}
    # definisikan bodynya
    mahasiswa_baru = {'nim' : 212, 'nama' : "joni"}
    # kirim request POST /mahasiswa
    conn.request('POST','/mahasiswa', body=json.dumps(mahasiswa_baru), headers=header)
    #dapatkan response nya
    resp = conn.getresponse().read()
    print(resp)

def edit_mahasiswa(nim):
    # kirim request get dengan url /mahasiswa
    # Inisiasi koneksi ke server
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # definisikan headernya
    header = {"Content-Type" : "application/json"}
    # definisikan bodynya
    mahasiswa_baru = {'nama' : "hahahaha", 'prodi' : "TEKKOM"}
    # kirim request POST /mahasiswa
    conn.request('PUT',"/mahasiswa/"+str(nim), body=json.dumps(mahasiswa_baru), headers=header)
    #dapatkan response nya
    resp = conn.getresponse().read()
    print(resp)

#tambah_mahasiswa()
edit_mahasiswa(155150201111108)
print("Data Mahasiswa : " + str(response))