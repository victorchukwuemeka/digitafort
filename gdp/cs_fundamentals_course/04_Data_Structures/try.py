class Node:
    def __init__(self,value , next=None):
        self.value = value
        self.next = next 


class LinkeList:
    def __init__(self):
        self.head = None 

    def insert_head(self, value):
        self.head = Node(value, self.head)

    def insert_tail(self,value):
        if self.head is None :
            self.head = Node(value)
            return 
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)

    def delete_node(self,)

        