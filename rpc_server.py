#author : erdiansahlan@student.ub.ac.id

# Import library xmlrpc server
import xmlrpc.server

# Inisiasi servernya
server = xmlrpc.server.SimpleXMLRPCServer(("0.0.0.0", 7778))

#Definisika fungsi yang akan dipanggil dari client
def penjumlahan(a, b):
    return(a+b)

def pengurangan(a, b):
    return(a-b)

def pembagian(a, b):
    return(a/b)

def perkalian(a, b):
    return(a*b)

def cek_prima(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True;
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True

    #penjumlahan, pengunrangan, pembagian, perkalian, cek bilangan prima
#tambahin method put delete di

# Daftarkan fungsi yang akan dipanggil dari client
server.register_function(penjumlahan, 'penjumlahan')
server.register_function(pengurangan, 'pengurangan')
server.register_function(perkalian, 'perkalian')
server.register_function(pembagian, 'pembagian')
server.register_function(cek_prima, 'cek_prima')

# Jalankan service servernya
server.serve_forever()