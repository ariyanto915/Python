from datetime import datetime, date
#from datetime import date
import calendar

lf="-";lol=60
presentime = datetime.now()

print("\nWaktu saat ini   :", presentime)
print(lf*lol)

tahun=int(input("Tanggal yang akan di cek \nMasukan Tahun      : "))
bulan=int(input("Masukan Bulan      : "))
tanggal=int(input("Masukan Tanggal    : "))

print(lf*lol)
print("")

calndr = calendar.month(tahun, bulan)
print(calndr)
#print("")

tgl_input = date(int(tahun),int(bulan),int(tanggal))
tgl_skr = date.today()

print(lf*lol)
print("Selisih hari dengan saat ini : ", tgl_input-tgl_skr)
print(lf*lol)
if tahun%400==0:
    print (tahun,"adalah Tahun Kabisat")
else:
    if tahun%100==0:
        print (tahun,"Bukan Tahun kabisat")
    else:
        if tahun%4==0:
            print (tahun,"adalah Tahun kabisat")
        else:
            print (tahun,"Bukan tahun kabisat")
print(lf*lol, "\n")