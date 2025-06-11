class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 


class LinkList:
    def __init__(self):
        self.head = None 
    

    def insert_new_node(self, data):
        new_node = Node(data) 

        if not self.head:
            self.head = new_node 
            return 
        
        # go last node 
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node 

        return self.head 
    
    def __str__(self):
        res = [] 
        
        current = self.head 

        while current:
            res.append(current.data) 
            current = current.next 
        
        return str(res) 



l = LinkList() 
l.insert_new_node('A') 
l.insert_new_node('B') 
l.insert_new_node('C') 
print(l) 