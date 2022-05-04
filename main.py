class Node:
    def __init__(self,value) -> None:
        self.value=value
        self.next=None
        self.previous=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def printit(self):
        B = self.head
        while B is not None:
            print(B.value)
            B=B.previous





nd = Node("monday")
nd2 =Node("tuesday")
nd3 =Node("wednesday")
ob = LinkedList()
ob.head = nd3
nd3.previous=nd2
nd2.previous=nd
ob.printit()