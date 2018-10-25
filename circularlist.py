class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLinkedlist():
    def __init__(self):
        self.head = None
    def printelement(self):
       print("Elements are:")
       temp = self.head
       while temp.next is not self.head :
            print(temp.data)
            temp = temp.next
       print("These are the elements")


Clist = CLinkedlist()

Clist.head = Node(1)
second = Node(2)
third = Node(3)
Clist.head.next = second
second.next = third
third.next = Clist.head
Clist.printelement()
