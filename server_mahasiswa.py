#author : erdiansahlan@student.ub.ac.id

#import library flask
from flask import Flask, request
import json

#inisiasi app flask sebagai server
app = Flask("Hello App")

data_mhs = [
	{
		"nim" : 155150200111092,
        "nama" : "Erdian Sahlan",
        "prodi" : "TIF"
	},
    {
        "nim" : 155150200111146,
        "nama" : "Miftaqul Novandi",
        "prodi" : "TIF"
    }
]

#mendefinisikan fungsi yang akan menghandle method GET dengan URL '/'
@app.route('/mahasiswa', methods=['GET'])
def handle_get():
    #Konversi dari list/dictionary ke string format JSON
    return json.dumps(data_mhs)

@app.route('/mahasiswa', methods=['POST'])
def tambah_mahasiswa():
    # Baca body request
    nim = request.json['nim']
    nama = request.json['nama']
    # Buat dictionary baru
    mahasiswa_baru = {
        'nama' : nama,
        'nim' : nim
    }
    #Tambahkan ke list data mahasiswa
    data_mhs.append(mahasiswa_baru)

    return("OK")

@app.route('/mahasiswa/<int:nim>', methods=['GET'])
def get_satu_mahasiswa(nim):
    for i,j in enumerate(data_mhs):
        if (data_mhs[i]['nim'] == nim):
            return json.dumps(data_mhs[i])

@app.route('/mahasiswa/hapus/<int:nim>', methods=['GET'])
def hapus_mahasiswa(nim):
    for i,j in enumerate(data_mhs):
        if (data_mhs[i]['nim'] == nim):
            data_mhs.pop(i)
    return "OK"

@app.route('/mahasiswa/<int:nim>', methods=['PUT'])
def edit_mahasiswa(nim):
    # Baca body request
    nama = request.json['nama']
    prodi = request.json['prodi']
    for i,j in enumerate(data_mhs):
        if (data_mhs[i]['nim'] == nim):
            data_mhs[i]["nama"] = nama
            data_mhs[i]["prodi"] = prodi

    return("OK")

#jalankan server flask
app.run(port=7777)