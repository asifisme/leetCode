class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

class linkedList:
    def __init__(self):
        self.head = None 
    
    def add(self, new_data):
        node = Node(new_data)
        node.next = self.head 
        node = self.head 
        return self.head 

l = linkedList()
l.add(5)
print(l)