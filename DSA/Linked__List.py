# linked list in python 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


# insert linked list node  
class linkedlist:
    def __init__(self):
        self.head = None 
    
    # inser function 
    def insert_node(self, data):
        new_node = Node(data) 
        
        # check the node is empty 
        if self.head is None:
            self.head = new_node
            return 
        
        # change the head 
        last_node = self.head 

        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node 
        
        # return the inserted linked list 
        return self.head 
    

    def inert_head(self, data):
        new_node = Node(data) 
        new_node.next = self.head 
        self.head =  new_node 

    
    def __str__(self):
        current = self.head 
        res = [] 
        while current:
            res.append(current.data) 
            current = current.next 
        return str(res)



# call the linked list 
l = linkedlist() 
l.insert_node(1) 
l.insert_node(3) 
l.insert_node(5) 
l.insert_node(6) 
l.inert_head(0)

print(l)