#author : erdiansahlan@student.ub.ac.id

import xmlrpc.client

# Koneksikan ke server RPC
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:7778/")

#panggil fungsinya
print("Hasil Penjumlahan 10+15 = "+ str(proxy.penjumlahan(10,15)))
print("Hasil Pengurangan 10-15 = "+ str(proxy.pengurangan(10,15)))
print("Hasil Perkalian 10+15 = "+ str(proxy.perkalian(10,15)))
print("Hasil Pembagian 10/15 = "+ str(proxy.pembagian(10,15)))
print("Apakah 10 bilangan prima? = "+ str(proxy.cek_prima(10)))
print("Apakah 11 bilangan prima? = "+ str(proxy.cek_prima(11)))