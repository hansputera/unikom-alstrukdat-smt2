###
# Quiz 1 - Algoritma dan Struktur Data 2
# Nama: HANIF DWY PUTRA S.
# NIM: 10125905
# Kelas: IF-10K
###

class Mahasiswa:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            bantu = self.head
            while bantu.next is not None:
                bantu = bantu.next
            bantu.next = node

    def show(self):
        bantu = self.head
        while bantu is not None:
            print(f"Name: {bantu.data.name}, Score: {bantu.data.score}")
            bantu = bantu.next

linkedList = LinkedList()

print("Data Nilai Mahasiswa Kelas Mugiwara")
print("=" * 30)

node1 = Node(Mahasiswa(name="Luffy", score=90))
node2 = Node(Mahasiswa(name="Zoro", score=85))
node3 = Node(Mahasiswa(name="Jinbe", score=80))
node4 = Node(Mahasiswa(name="Sanji", score=75))
node5 = Node(Mahasiswa(name="Im Sama", score=95))
node6 = Node(Mahasiswa(name="Joyboy", score=100))

linkedList.append(node1)
linkedList.append(node2)
linkedList.append(node3)
linkedList.append(node4)
linkedList.append(node5)
linkedList.append(node6)

linkedList.show()

print("Created by : 10125905 - HANIF DWY PUTRA S.")