class Node:
    def __init__(self, value):
        self.data = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 


    def inset_node(self, value):
        new_node = Node(value=value)

        if self.head is None:
            self.head = new_node 
            return 
        
        current = self.head 

        while current.next:
            current = current.next 
        current.next = new_node 

    def new_head(self):
        new_data = Node(100)
        new_data.next = self.head 
        self.head = new_data

        return self.head 
    
    def swap_node(self):
        second_node = self.head.next 
        self.head.next = second_node.next 
        second_node.next = self.head 
        self.head = second_node 

    
    def __str__(self):
        res = []
        current = self.head 
        while current:
            res.append(current.data)
            current = current.next 
        return str(res) 
    
head = [1,2,3,4] 

l = LinkedList()

for i in head:
    l.inset_node(i) 

l.new_head()
l.swap_node()

print(l)
        
