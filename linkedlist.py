class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def pushelements(self, val):
        for i in range(0,val):
            if i is 0 :
                self.head = input()
                self.head.next = temp
            else:
                 
                 temp.data = input()
                 temp = temp.next 

    def printelements(self):
        n = len(self)
        temp = self.head
        for i in range(0,n):
            print(temp.data)
            temp = temp.next
 
llist = LinkedList()
llist.pushelements(5)
llist.printelements()

   
