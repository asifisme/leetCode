# linked list all operation in python programming languages 
class Node:
    def __init__(self, data : int):
        self.data = data 
        self.nextNode = None 

# call Node and make list 
class Linked_list:
    def __init__(self):
        self.head = None 
    
    def insert_node(self, data, at_head=False):
        new_node = Node(data) 

        # check head is empty 
        if self.head is None:
            self.head = new_node 
            return 
        
        # add new head in the linked list 
        if at_head:
            new_node.nextNode = self.head 
            self.head = new_node 
            return 
        
        # insert new node in linked list 
        last_node = self.head 
        while last_node.nextNode : 
            last_node = last_node.nextNode 
        last_node.nextNode = new_node 
        return self.head 
    
    # insert after  
    def insert_after(self, data, targeted_after):
        current = self.head 
        while current:
            if current.data == targeted_after:
                new_node = Node(data) 
                new_node.nextNode = current.nextNode 
                current.nextNode = new_node 
                return 
            current = current.nextNode 
        


    # delete in a specific node 
    def delete_node(self, key):
        temp = self.head 

        # if the key is first item 
        if temp.data == key:
            self.head = temp.nextNode 
            temp = None
            return self.head 
        
        # if the key is not first item 
        while temp:
            if temp.data == key:
                break 
            prev = temp 
            temp = temp.nextNode 
        
        if temp == None:
            return  

        prev.nextNode = temp.nextNode 
        temp = None 


    # print the linked list as a string 
    def __str__(self):
        res = [] 
        current = self.head 
        while current:
            res.append(current.data) 
            current = current.nextNode 
        return str(res) 


# call linked 

l = Linked_list() 
l.insert_node(2)
l.insert_node(3)
l.insert_node(4)
l.insert_node(5) 
l.insert_node(6) 
l.insert_node(1, True)
l.delete_node(6)
l.insert_after(4, 3)
# l.delete_node(1)

print(l)