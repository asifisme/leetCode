
class Node:
    def __init__(self, data: int):
        self.data = data 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None 
    

    def insert_new_node(self, data):
        new_node = Node(data=data) 

        if not self.head:
            self.head = new_node 
            return 
        

        last_node = self.head 

        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node 

        return self.head 
    
    
    def delete_index_node(self, index):
        curr = self.head 

        for _ in range(index):
            curr = curr.next 
        
        if not curr:
            return self.head.next 
        
        sec = self.head 

        while curr.next:
            sec = sec.next 
            curr = curr.next 
        
        sec.next = sec.next.next 

        return self.head 
           
    

    def __str__(self):
        res = [] 
        current_node = self.head 
        while current_node:
            res.append(current_node.data) 
            current_node = current_node.next 
        
        return str(res) 
    


l = LinkedList() 
l.insert_new_node(1)
# l.insert_new_node(2) 
# l.insert_new_node(3) 
# l.insert_new_node(4) 
# l.insert_new_node(5)
l.delete_index_node(1) 
print(l) 