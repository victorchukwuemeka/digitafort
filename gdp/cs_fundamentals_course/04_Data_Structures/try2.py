
class Stack:
    def __init__(self):
        self.items = []

    #add data to our list
    def push(self, value):
        self.items.append(value)


    #deleting data
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    #get view the data
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    #checking if the list is empty
    def is_empty(self):
        return len(self.items) == 0

    #checking the size
    def size_check(self):
        return len(self.items)


    
