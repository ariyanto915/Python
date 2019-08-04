print ("Menghitung Pecahan")
print ("[1] Penjumlahan \n[2] Pengurangan \n[3] Perkalian \n[4] Pembagian")
pilih = int(input("Masukan Pilihan (1-4) : "))

b1 = int(input("Masukan bulat 1 :"))

pm1 = int(input("Masukan Pembilang 1 : "))
py1 = int(input("Masukan Penyebut  1 : "))
b2 = int(input("Masukan bulat 2 :"))
pm2 = int(input("Masukan Pembilang 2 : "))
py2 = int(input("Masukan Penyebut  2 : "))
print (" ", pm1, " ", " ", pm2, " ")
print (b1 , "-", "+", b2 , "-", " ")
print (" ", py1, " ", " ", py2, " ")
print ("+-------------+")
if pilih == 1 :
    pm1 = (py1 * b1) + pm1
    pm2 = (py2 * b2) + pm2
    print (pm1, " ", pm2),
    print ("-" , "+" , "-"),
    print (py1 , " " , py2),
    print ("+-------------+")
    py = (py1 * py2)
    pm1 = (py / py1) * pm1
    pm2 = (py / py2) * pm2
    pm = pm1 + pm2
    print (pm1 , " " , pm2 , " " , pm)
    print ("-" , "+" , "-" , "=" , "-")
    print (py  , " " , py  , " " , py)

elif pilih == 2 :
    pm1 = (py1 * b1 ) + pm1
    pm2 = (py2 * b2) + pm2
    print (pm1 , " " , pm2)
    print ("-" , "-" , "-")
    print (py1 , " " , py2)
    print ("+-------------+")
    py = py1 * py2
    pm1 = (py / py1) * pm1
    pm2 = (py / py2) * pm2
    pm = pm1 - pm2
    print (pm1 , " " , pm2 , " " , pm)
    print ("-" , "-" , "-" , "=" , "-")
    print (py  , " " , py  , " " , py)

elif pilih == 3 :
    pm1 = (py1 * b1 ) + pm1
    pm2 = (py2 * b2) + pm2
    print (pm1 , " " , pm2)
    print ("-" , "X" , "-")
    print (py1 , " " , py2)
    print ("+-------------+")
    pm = pm1 * pm2
    py = py1 * py2
    print (pm1 , " " , pm2 , " " , pm)
    print ("-" , "X" , "-" , "=" , "-")
    print (py1 , " " , py2 , " " , py)

elif pilih == 4 :
    pm1 = (py1 * b1 ) + pm1
    pm2 = (py2 * b2) + pm2
    print (pm1 , " " , pm2)
    print ("-" , ":" , "-")
    print (py1 , " " , py2)
    print ("+-------------+")
    pm = pm1 * py2
    py = py1 * pm2
    print (pm1 , " " , py2 , " " , pm)
    print ("-" , "X" , "-" , "=" , "-")
    print (py1 , " " , pm2 , " " , py)
else:
    print ("Pilihan yang anda masukan salah")
