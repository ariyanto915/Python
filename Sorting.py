list=[] #deklarasi list sebagai array

def swap(a,b):
    list[a],list[b]=list[b],list[a]

def awal():

    print ("Ariyanto")
    print ("18364003")
    print ("Program Sorting \n")
    print ("Menu Pilihan")
    print ("1. Create Program")
    print ("2. Exit")
    
    data=input ("masukan pilihan :")
    if data=='1':
        array()
    elif data=='2':
        exit()


def array():
    jumlah= int(input("\nBanyak Data : "))
    awal=0
    while (awal<jumlah): 
        awal=awal+1
        bil=input("input data ke-%d:"%awal)
        list.append(bil) 
    print ("data acak =", list)
    pilih(jumlah)
    
def pilih(jumlah):   
    print ("\nPilih Jenis Sorting :")
    print ("1) Bubble sort")
    print ("2) Sekection sort")
    print ("3) Quick sort")
    print ("4) Insertion sort")
    print ("5) Exchange sort")
    choice=input("Pilihan =")
    tipe(choice,jumlah)
    
def tipe(pilih,jumlah):
    print ("\n1) Ascending")
    print ("2) Descending")
    p=input("Tipe yang dipilih :")
    if pilih=='1':
        bubble(p,jumlah)
    elif pilih=='2':
        quick(p,jumlah)
    elif pilih=='3':
        select(p,jumlah)
    elif pilih=='4':
        insert(p,jumlah)
    elif pilih=='5':
        exchange(p,jumlah)

def bubble(p,jumlah):  
    for a in range(0,jumlah):
            for b in range(1,jumlah):
                if p=='1':
                   if list[b]<list[b-1]:
                       swap(b,b-1)
                else:
                    if list[b]>list[b-1]:
                         swap(b,b-1)
    print (list)

def select(p,jumlah):                        
    for awal in range(0,jumlah):
            pos=awal
            for k in range(awal,jumlah):
                    if p=='1':
                        if list[k]<list[pos]:
                                    pos=k
                    else:
                        if list[k]>list[pos]:
                                    pos=k
            if pos!=awal:
                    swap(pos,awal)
    print (list)

def quicksort(left,right,p):
        l=left
        r=right
        pivot=list[left]
        while(left<right):
                if p=='1':
                        while((list[right]>=pivot) and left<right):
                                right=right-1
                        if(left!=right):
                                list[left]=list[right]
                                left=left+1
                        while((list[left]<=pivot) and left<right):
                                left=left+1
                        if(left!=right):
                                list[right]=list[left]
                                right=right-1
                else:
                        while((list[right]<=pivot) and left<right):
                                right=right-1
                        if(left!=right):
                                list[left]=list[right]
                                left=left+1
                        while((list[left]>=pivot) and left<right):
                                left=left+1
                        if(left!=right):
                                list[right]=list[left]
                                right=right-1
        list[left]=pivot
        pivot=left
        left=l
        right=r
        if left<pivot:
                quicksort(left,pivot-1,p)
        if right>pivot:
                quicksort(pivot+1,right,p)

def quick(p,jumlah):
        quicksort(0,jumlah-1,p)
        print (list)

def insert(p,jumlah):                        
    for awal in range(1,jumlah):
        temp=list[awal]
        jumlah=awal-1
        if p=='1':
                while list[jumlah]>temp and jumlah>=0:
                        list[jumlah+1]=list[jumlah]
                        jumlah=jumlah-1
        else:
                while list[jumlah]<temp and jumlah>=0:
                        list[jumlah+1]=list[jumlah]
                        jumlah=jumlah-1
        list[jumlah+1]=temp
    print (list)

def exchange(p,jumlah):                  
    for awal in range(jumlah-1):
        for k in range(awal+1,jumlah):
            if p=='1':
                if list[k]<list[awal]:
                    swap(k,awal)
    else:
        if list[k]>list[awal]:
            swap(k,awal)
    print (list)
awal()
