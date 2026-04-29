#class for circula Q
class c_q:
    #constructor
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    #adding data to q
    def enqueue(self,item):
        #check if queue is full
        if self.is_full():
            raise OverflowError("queue is full")
        #add data to the queue
        #modula arithimetic
        self.rear =(self.rear+1) % self.capacity
        self.queue[self.rear] = item
        if self.front == -1:
            self.front = 0
        self.size += 1

    #removing data from q
    def  dequeue(self):
        #check if queue is empty
        if self.size == 0:
            raise IndexError("c q is empty")


    def is_full(self):
        return self.size == self.capacity
