
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_new_node(self, data):
        new_node = Node(data) 

        if not self.head:
            self.head = new_node 
            return 
        
        current = self.head 

        while current.next:
            current = current.next 
        current.next = new_node 

        return self.head 
    
    def delete_Node_item(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next 
            return self.head 
        
        current = self.head 
        prev = None 

        while current:
            if current.data == data:
                prev.next = current.next 
            prev = current 
            current = current.next 

        return self.head 

    def Remove_all_duplicate(self):
        current = self.head 
        while current:
            while current.next and current.data == current.next.data:
                current.next = current.next.next 
            current = current.next 

    def RemoveAllDuplicate(self):
        data_map = {}
        current = self.head 
        while current:
            if current.data not in data_map:
                data_map[current.data] = 1 
            else:
                data_map[current.data] += 1 
            current = current.next 

        for key, value in data_map.items():
            if value >= 2:
                self.delete_Node_item()
            
        
        return data_map 

    def __str__(self):
        res  = [] 
        current = self.head 
        while current:
            res.append(current.data)
            current = current.next 
        return str(res) 
    


head = [1,2,3,3,4,4,5]

l = LinkedList()

for item in head:
    l.insert_new_node(item)

print(l)
# l.delete_Node_item(2)
l.Remove_all_duplicate()
# print(l.RemoveAllDuplicate())
print(l)