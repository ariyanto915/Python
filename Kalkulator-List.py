list1 = []
list2 = []
tambah = []
kurang = []
kali = []
bagi = []
mod = []

angka = int(input("Masukan jumlah element : "))
print("Masukan nilai element nya  ")
for i in range(1, angka + 1):
    nilailist1 = int(input("Masukan nilai element ke %d untuk List1 : " %i))
    list1.append(nilailist1)

    nilailist2 = int(input("Masukan nilai element ke %d untuk List2 : " %i))
    list2.append(nilailist2)

for j in range(angka):
    tambah.append( list1[j] + list2[j])
    kurang.append( list1[j] - list2[j])
    kali.append( list1[j] * list2[j])
    bagi.append( list1[j] / list2[j])
    mod.append( list1[j] % list2[j])

print("\nList1 = ",list1)
print("List2 = ",list2)

print("\nList setelah tambah      =  ", tambah)
print("List setelah kurang      =  ", kurang)
print("List setelah di kali     =  ", kali)
print("List setelah di bagi     =  ", bagi)
print("List setela di modulus   =  ", mod)
