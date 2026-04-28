#Program Circular_Linked_List_Hitung_Genap_Ganjil

class SimpulAngka:
    def __init__(self, info):
        self.info = info
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.awal = None
        self.akhir = None

    def tambah(self, info):
        simpul = SimpulAngka(info)
        if self.awal is None:
            self.awal = simpul
            self.akhir = simpul
        else:
            simpul.prev = self.akhir
            self.akhir.next = simpul
            self.akhir = simpul

    def hitung_genap_ganjil(self):
        ctr_genap  = 0
        ctr_ganjil = 0
        bantu = self.awal

        while bantu is not None:
            if bantu.info % 2 == 0:
                ctr_genap += 1
            else:
                ctr_ganjil += 1
            bantu = bantu.next

        print(f"Banyaknya Angka Genap  = {ctr_genap} buah")
        print(f"Banyaknya Angka Ganjil = {ctr_ganjil} buah")

ll = LinkedList()
ll.tambah(9)
ll.tambah(2)
ll.tambah(7)

ll.hitung_genap_ganjil()
print("\nCreated by HANIF DWY PUTRA S. (NIM: 10125905)")
