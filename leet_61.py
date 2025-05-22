class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert_node(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node 
            new_node.next = self.head 
            return 
        
        current = self.head 
        while current.next != self.head:
            current = current.next 
        
        current.next = new_node 
        new_node.next = self.head 
        return self.head 
    
    def Rotate(self, k):
        if not self.head or k == 0:
            return 
        
        # current = self.head 

        # count = 1 

        # while current.next != self.head:
        #     count += 1 
        #     current = current.next 
        
        # k = k % count 

        # if k == 0:
        #     return 
        
        temp = self.head 
        for _ in range(k):
            temp = temp.next 
        self.head = temp 


    def __str__(self):
        res = []
        current = self.head 
        while True:
            res.append(current.value) 
            current = current.next 
            if current == self.head:
                break 
        return str(res)
    
head = [1,2,3,4,5]
k = 2

l = LinkedList()
for i in head:
    l.insert_node(i) 

l.Rotate(2)

print(l) 