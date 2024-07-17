# linked list in pythoh 

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    # insert node in the list 
    def insert_node(self, data):
        new_node = Node(data) 

        if self.head is None:
            self.head = new_node 
            return 
        
        last_node = self.head 
        while last_node.next:
            last_node = last_node.next 
        last_node.next = new_node

        return self.head 

    def At_head(self, data):
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node
    
    def Search_value(self, search_data): 
        temp = self.head 
        res = []
        count = 0

        if temp:
            while temp.next:
                if temp.data == search_data:
                    res.append([temp.data, count])
                    count += 1
                    break 
                temp = temp.next 
        return print(res)

    
    def __str__(self):
        res = [] 
        current = self.head 
        while current:
            res.append(current.data) 
            current = current.next 
        return str(res) 


l = LinkedList() 

l.insert_node(1) 
l.insert_node(3) 
l.insert_node(2) 
l.insert_node(4)
l.At_head(5) 
l.At_head(3)
l.At_head(3)

l.Search_value(3)

print(l)