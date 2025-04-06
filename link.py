# 15.07 
class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None 
        self.prev = None 

node1   = Node(3)
node2   = Node(5) 
node3   = Node(7) 
node4   = Node(9) 

node1.next = node2 
node2.next = node3 
node3.next = node4 

node2.prev = node1
node3.prev = node2 
node4.prev = node3


current_node = node1 

while current_node:
    print(current_node.data, end='->') 
    current_node = current_node.next 
print('null')

current_node = node4 
while current_node:
    print(current_node.data, end='->') 
    current_node = current_node.prev 
print('null')