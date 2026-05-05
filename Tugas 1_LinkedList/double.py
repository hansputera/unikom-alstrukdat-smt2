class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubledLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAwal(self, data):
        node = Node(data)
        node.next = self.head

        if self.head is not None:
            self.head.prev = node
        else:
            self.tail = node

        self.head = node

    def insertAkhir(self, data):
        node = Node(data)
        node.prev = self.tail

        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node

    def hapus(self, data):
        bantu = self.head
        while bantu is not None and bantu.data != data:
            bantu = bantu.next

        if bantu is None:
            return False

        if bantu.prev is not None:
            bantu.prev.next = bantu.next
        else:
            self.head = bantu.next

        if bantu.next is not None:
            bantu.next.prev = bantu.prev
        else:
            self.tail = bantu.prev

        return True

    def tampilMaju(self):
        bantu = self.head
        while bantu is not None:
            print(bantu.data)
            bantu = bantu.next

    def tampilMundur(self):
        bantu = self.tail
        while bantu is not None:
            print(bantu.data)
            bantu = bantu.prev

doubleLinkedList = DoubledLinkedList()
doubleLinkedList.insertAwal(10)
doubleLinkedList.insertAkhir(25)
doubleLinkedList.insertAkhir(30)
doubleLinkedList.insertAkhir(47)

doubleLinkedList.hapus(25)

doubleLinkedList.tampilMundur()