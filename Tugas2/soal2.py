class SimpulAngka:
    def __init__(self, info):
        self.info = info
        self.prev = None
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.awal = None
        self.akhir = None

    def tambah(self, info):
        simpul = SimpulAngka(info)
        if self.awal is None:
            self.awal = simpul
            self.akhir = simpul
            simpul.next = simpul
            simpul.prev = simpul
        else:
            simpul.prev = self.akhir
            simpul.next = self.awal
            self.akhir.next = simpul
            self.awal.prev = simpul
            self.akhir = simpul

    def tampil(self):
        if self.awal is None:
            print("List kosong!")
            return
        bantu = self.awal
        hasil = []
        while True:
            hasil.append(str(bantu.info))
            bantu = bantu.next
            if bantu == self.awal:
                break

    def hitung_bawah_rata_rata(self):
        if self.awal is None:
            print("List kosong!")
            return

        total = 0
        n     = 0
        bantu = self.awal

        while True:
            total += bantu.info
            n     += 1
            bantu  = bantu.next
            if bantu == self.awal:
                break

        rata_rata = total / n
        ctr   = 0
        bantu = self.awal

        while True:
            if bantu.info < rata_rata:
                ctr += 1
            bantu = bantu.next
            if bantu == self.awal:
                break

        print(f"Banyaknya angka yang dibawah rata-rata = {ctr} buah angka")


cll = CircularLinkedList()
cll.tambah(2)
cll.tambah(12)
cll.tambah(8)

cll.tampil()
cll.hitung_bawah_rata_rata()
print("\nCreated by HANIF DWY PUTRA S. (NIM: 10125905)")