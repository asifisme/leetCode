

""" 
 -> Node contain two things 1. data 2. link that connect with another node  

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None  


    def insert_at_begin(self, data):
        new_node = Node(data=data)

        if not self.head:
            self.head = new_node 
            return 
        else:
            new_node.next = self.head 
            self.head = new_node 

    
    def insert_at_index(self, data, index):

        if index == 0:
            self.insert_at_begin(data=data) 
            return 
        
        position = 0 
        current_node = self.head 
        while not current_node and position + 1 != index:
            position += 1 
            current_node = current_node.next 

            if not current_node:
                new_node = Node(data=data) 
                new_node.next = current_node.next 
                current_node.next = new_node 

