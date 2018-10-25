class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.capacity = capacity
        self.Q = [None]*capacity
    
    def Enqueue(self, val):
        if self.size == self.capacity:
            print("Queue is full")
            return 
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = val
        self.size = self.size + 1

    def Dequeue(self):
        if self.size == 0:
            print("Empty queue")
            return
        print("Dequeued element: %s"  %str(self.Q[self.front]))
        self.front = (self.front +1) % self.capacity
        self.size = self.size - 1

    def printelements(self):
        temp = 0
        while temp < self.size:
            print("Element: %s" %str(self.Q[temp]))
            temp = temp + 1

queue = Queue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
queue.Enqueue(50)
queue.Enqueue(60)
queue.printelements()
