def dec(num, binNr):
    if num <=1:
        return str(num%2)+binNr

    binNr = str(num%2)+binNr
    return dec(num // 2, binNr)

print('Konversi Desimal ke Binary')
nilai=int(input("Masukan nilai yang akan dikonversi : "))
#number=100
print('Number: %d' %nilai)

Bin = dec(nilai, "")
print('Bin : %s' %Bin)
