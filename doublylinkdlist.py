class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublelinkedList:
    def __init__(self):
        self.head = None 
    
dlist = doublelinkedList()

dlist.head = Node(1)
second = Node(2)
dlist.head.next = second
dlist.head.prev = None

third = Node(3)
second.next =third
third.prev = second
third.next = None

temp = dlist.head
for i in range(0,3):
    print("data: ")
    print(temp.data)
    if temp.next != None:
        temp = temp.next

