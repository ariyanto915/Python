import os
 
class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
class DoubleList(object):
 
    head = None
    tail = None        
    def menuTambah(self):
        os.system('clear')
        temp = int(input('Masukkan data baru = '))
        new_node = Node(temp, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
   
    def menuHapus(self):
        os.system('clear')
        temp = int(input('Masukkan data yang akan dihapus = '))
        current_node = self.head
       
        while current_node is not None:
            if current_node.data == temp:
                if current_node.next is None:
                    current_node.prev.next = None
                elif current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    self.head = current_node.next 
                    current_node.next.prev = None 
 
            current_node = current_node.next

    def menuTampil(self):
        os.system('clear')
        print ("Tampilkan list data:")
       
        current_node = self.head
        while current_node is not None:
            print (current_node.prev.data) if hasattr(current_node.prev, "data") else None,
            print (current_node.data),
            print("   ->"),
            print (current_node.next.data) if hasattr(current_node.next, "data") else None
            current_node = current_node.next
           
    def menuUmum(self):
        pilih = "y"
        while ((pilih == "y") or (pilih == "Y")):
            os.system('clear')
            print('Pilih menu yang anda inginkan')
            print('==============================')
            print('1 : Tambah data ke linked list')
            print('2 : Hapus data di linked list')
            print('3 : Tampilkan data di linked list')
            print('4 : Keluar Program')
            pilihan = str(input("Masukkan Menu yang anda pilih = "))
            if(pilihan == "1"):
                self.menuTambah()
            elif(pilihan == "2"):
                self.menuHapus()
            elif(pilihan == "3"):
                self.menuTampil()
                x = input("")
            else :
                pilih ="n"
               
if __name__ == "__main__":
    d = DoubleList()
    d.menuUmum()
