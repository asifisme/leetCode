# linked list in python 
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_node(self, data):
        new_node = Node(data) 

        # check the head is empty 
        if self.head is None:
            self.head = new_node 
            return  
        
        # insert data in node 
        last_node = self.head 
        while last_node.next : 
            last_node = last_node.next 
        last_node.next = new_node 
        return self.head 
    
    # insert head 
    def insert_head(self, data):
        new_head = Node(data) 
        new_head.next = self.head 
        self.head = new_head 
        return 
    
    # insert in middle 
    def insert_middle(self, data):
        middle_node = Node(data) 
        current = self.head 
        
        while current:
            if current.data == 3:
                middle_node.next = current
                break 
            current = current.next 
        return  
    
    # delete the specfic node 
    def delete_node(self, key):
        temp = self.head 

        # if head hold the key 
        if temp.data == key:
            self.head = temp.next 
            temp = None 
            return 
        
        # if head is not hold the key 
        while temp:
            if temp.data == key:
                break 
            prev = temp 
            temp = temp.next 
        
        if temp == None:
            return 
        
        prev.next = temp.next 
        temp = None 


    # all data convert in a string 
    def __str__(self):
        res = [] 
        current = self.head 
        while current:
            res.append(current.data) 
            current = current.next 
        return str(res) 


# call the linked list and insert data 
l = LinkedList() 
l.insert_node(1) 
l.insert_node(2) 
l.insert_node(3) 
l.insert_node(4) 
l.insert_node(5) 
# l.insert_head(10)
l.delete_node(4)
print(l)