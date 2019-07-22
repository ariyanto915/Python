import os
 
class Node(object):
 
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
   
    def get_data(self):
        return self.data
   
    def get_next(self):
        return self.next_node
   
    def set_next(self, new_next):
        self.next_node = new_next
       
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
   
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
 
    def size(self):
        sekarang = self.head
        count = 0
        while sekarang:
            count += 1
            sekarang = sekarang.get_next()
        return count
 
    def search(self, data):
        sekarang = self.head
        hasil = False
        while sekarang and hasil is False:
            if sekarang.get_data() == data:
                hasil = True
            else:
                sekarang = sekarang.get_next()
               
        return hasil
 
    def delete(self, data):
        sekarang = self.head
        sebelumnya = None
        hasil = False
        while sekarang and hasil is False:
            if sekarang.get_data() == data:
                hasil = True
            else:
                sebelumnya = sekarang
                sekarang = sekarang.get_next()
        if sekarang is None:
            raise ValueError("Data tidak ada di dalam list")
        if sebelumnya is None:
            self.head = sekarang.get_next()
        else:
            sebelumnya.set_next(sekarang.get_next())
 
    def showData(self):
        os.system('clear')
        print ("Tampilkan list data:")
        print ("Node -> Next Node")
        node = self.head
        while node is not None:
            print (node.data),
            print ("   ->"),
            print (node.next_node.data) if hasattr(node.next_node, "data") else None
           
            node = node.next_node
 
    def menu(self):
        pilih = "y"
        while (pilih == "y"):
            os.system("clear")
            print("===============================")
            print("|  Menu aplikasi linked list  |")
            print("===============================")
            print("1. Insert data")
            print("2. Delete data")
            print("3. Cari data")
            print("4. Panjang dari linked list")
            print("5. Tampil data")
            print("===============================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda tambahkan: "))
                self.insert(obj)
            elif(pilihan=="2"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda dihapus: "))
                self.delete(obj)
                x = input("")
            elif(pilihan=="3"):
                os.system("clear")
                obj = str(input("Masukan data yang ingin anda dicari: "))
                status = self.search(obj)
                if status == True:
                    print("Data ditemukan pada list")
                else:                  
                    print("Data tidak ditemukan")
                x = input("")
            elif(pilihan=="4"):
                os.system("clear")
                print("Panjang dari queue adalah: "+str(self.size()))
                x = input("")
            elif(pilihan=="5"):
                os.system("clear")
                self.showData()
                x = input("")
            else:
                pilih="n"
 
if __name__ == "__main__":
    l = LinkedList()
    l.menu()