class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAwal(self, data):
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
        else:
            bantu = self.head
            while bantu.next != self.head:
                bantu = bantu.next
            node.next = self.head
            node.prev = bantu
            self.head.prev = node
            bantu.next = node
            self.head = node

    def insertAkhir(self, data):
        node = Node(data)
        if self.head == None:
            node.next = node
            node.prev = node
            self.head = node
            return
        bantu = self.head
        while bantu.next != self.head:
            bantu = bantu.next
        bantu.next = node
        node.prev = bantu
        node.next = self.head
        self.head.prev = node

    def tampilkan(self):
        bantu = self.head
        while True:
            print(bantu.data)
            if bantu.next == self.head:
                break
            bantu = bantu.next

    def tampilkanMundur(self):
        bantu = self.head.prev
        while True:
            print(bantu.data)
            if bantu == self.head:
                break
            bantu = bantu.prev

circular = CircularLinkedList()
circular.insertAwal(10)
circular.insertAkhir(25)
circular.insertAkhir(30)
circular.insertAkhir(47)

# circular.tampilkan()
circular.tampilkanMundur()