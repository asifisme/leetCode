

class Node:
    def __init__(self, value):
        self.data = value 
        self.next = None 



class LinkedList:
    def __init__(self):
        head = None 

    
    def insert_new_node(self, value)-> Node:
        new_node = Node(value) 

        if not self.head:
            self.head = new_node 
            return 
        
        current = self.head 

        while current.next:
            current = current.next 
        current.next = new_node 
        return self.head 
    
    def addTwoNumber(self, l1: Node, l2: Node)-> Node: 
        dummy_node = Node(0) 
        current = dummy_node 
        carry = 0 

        while carry or l1 or l2: 
            if l1:
                carry += l1.data 
                l1 = l1.next 
            
            if l2:
                carry += l2.data 
                l2 = l2.next 

            current.next = Node(carry % 10) 
            carry //= 10 
            current = current.next 
        return dummy_node.next 
    