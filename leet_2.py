class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_new_node(self, data):
        node_n = Node(data) 

        if self.head is None:
            self.head = node_n 
            return 
        
        current = self.head 
        while current.next:
            current = current.next 
        current.next = node_n
        return self.head 
    
    # def add_two_number(self):
    #     val_one = ""
    #     val_two = 0 

    #     current = self.head 
    #     while current:
    #         val_one += str(current.data)
    #         current = current.next 

    #     return val_one[::-1]

    def __str__(self):
        res = [] 
        current = self.head 
        while current:
            res.append(current.data) 
            current = current.next 

        return str(res) 

l = LinkedList() 
l.insert_new_node(2) 
l.insert_new_node(4)
l.insert_new_node(3) 

m = LinkedList() 
m.insert_new_node(5)
m.insert_new_node(6) 
m.insert_new_node(4) 


class Soluation:
    def add_two_number(self, list_one : Node, list_two: Node):
        val_one = '' 
        current_one = list_one
        while current_one:
            val_one += str(current_one.data) 
            current_one = current_one.next 
        
        val_two = ''
        current_two = list_two 
        while current_two:
            val_two += str(current_two.data) 
            current_two = current_two.next 
        
        total = int(val_one[::-1]) + int(val_two[::-1]) 

        dummy = Node(0) 
        current = dummy 
        for digit in str(total)[::-1]:
            current.next = Node(int(digit)) 
            current = current.next 

        return dummy.next 

        
    

s = Soluation()
result = s.add_two_number(l.head, m.head)  
print(result)

        
        




# print(l) 

# print(m) 







# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.