class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # None = NULL

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAwal(self, node: Node):
        node.next = self.head
        self.head = node

    def insertAkhir(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            bantu = self.head
            while bantu.next is not None:
                bantu = bantu.next
            bantu.next = node

    def remove(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        bantu = self.head
        while bantu.next is not None and bantu.next.data != data:
            bantu = bantu.next

        if bantu.next is not None:
            bantu.next = bantu.next.next

    def tampilkan(self):
        bantu = self.head
        while bantu is not None:
            print(bantu.data)
            bantu = bantu.next


linkedList = LinkedList()

node1 = Node(10)
node2 = Node(25)
node3 = Node(30)
node4 = Node(47)

linkedList.insertAwal(node1)
linkedList.insertAkhir(node2)
linkedList.insertAkhir(node3)
linkedList.insertAkhir(node4)

linkedList.remove(30)

linkedList.tampilkan()
