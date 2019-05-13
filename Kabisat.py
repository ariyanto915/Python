tahun=input('Masukkan Tahun = ')
tahun=int(tahun)
if tahun%400==0:
    print (tahun,"Tahun Kabisat")
else:
    if tahun%100==0:
        print (tahun,"Bukan tahun kabisat")
    else:
        if tahun%4==0:
            print (tahun,"Tahun kabisat")
        else:
            print (tahun,"Bukan tahun kabisat")
