class Node:
    __slots__ = ("info", "next")

    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    __slots__ = ("awal",)

    def __init__(self):
        self.awal = None

    def isEmpty(self):
        return self.awal is None

    def TampilData(self):
        bantu = self.awal
        if bantu is None:
            print("Isi Linked List : Data Kosong")
            return

        parts = []
        append = parts.append

        while True:
            append(str(bantu.info))
            bantu = bantu.next
            if bantu is None:
                break
            append(" -> ")

        print("Isi Linked List :", "".join(parts))

    def BanyakNode(self):
        bantu = self.awal
        count = 0

        while bantu:
            count += 1
            bantu = bantu.next

        return count

    def Penghancuran(self):
        self.awal = None


list1 = LinkedList()

node1 = Node(5)
node2 = Node(7)
node3 = Node(2)
node4 = Node(10)

list1.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4

list1.TampilData()
print("Banyak Data :", list1.BanyakNode())

list1.Penghancuran()
list1.TampilData()
print("Banyak Data :", list1.BanyakNode())

print("=" * 30)
print("Created by HANIF DWY PUTRA S. (NIM: 10125905)")
print("Tanggal Pengerjaan: 08 April 2026 (08/04/2026)")
print("=" * 30)