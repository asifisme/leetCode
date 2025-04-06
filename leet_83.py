class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
    

class LinkedList:
    def __init__(self):
        self.head = None 
    

    def insert_new_node(self, data):
        new_node = Node(data=data) 

        # check the head 
        if not self.head:
            self.head = new_node 
            return 
        

        # exchange head 
        current = self.head 
        while current.next:
            current = current.next 
        current.next = new_node 

    def remove_item(self, data):
        
        if self.head and  self.head.data == data:
            self.head = self.head.next 
            return self.head 
        
        current = self.head 
        while current:
            if current.data == data:
                current = current.next 
                return self.head 
            current = current.next 
        
        return self.head 
    
    def removeAnyDuplicate(self):
        seen = set()
        current = self.head 
        prev = None 

        # while current:
        #     if current.data in seen:
        #         prev.next = current.next 
        #     else:
        #         seen.add(current.data)
        #         prev = current 

        while current:
            while current.next and current.data == current.next.data:
                current.next = current.next.next 
            current = current.next 
        
        return self.head 
    
    # print the value of linked list in terminal 
    def __str__(self):
        res = [] 
        current = self.head 
        while current:
            res.append(current.data)
            current = current.next  

        return str(res) 

l = LinkedList()
l.insert_new_node(1)
l.insert_new_node(1)
l.insert_new_node(1)
l.insert_new_node(2)
l.insert_new_node(2)
l.insert_new_node(2)
l.insert_new_node(2)
l.insert_new_node(3)
l.insert_new_node(3)
# l.remove_item(3)
print(l)
l.removeAnyDuplicate()

print(l)