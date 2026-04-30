import heapq


class Pq:
    def __init__(self):
        self.heap = []
    
    #adding the item and state of importance
    def enq(self, item, p):
        #adding the data to our tree structure 
        heapq.heappush(self.heap, (p,item))

    def deq(self):
        #CHECK IF DATA EXIST 
        if self.heap == None :
            return None
        #removing the data fromthe structure
        p,i = heapq.heappop(self.heap)
        return i
    #get view the item 
    def peek(self):
        if self.q_empty:
            return IndexError("P ")
        return self.heap[0][1]
        
    
    # check the data
    def q_empty(self):
        return len(self.heap) == 0
    
    #side of the q
    def size_q(self):
        return len(self.heap)
    

q = Pq()
q.enq("low ", 3)
q.enq("fast", 1)
q.enq("slow", 2)
print(q)