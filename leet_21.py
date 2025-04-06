
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_node(self, data):
        new_node = Node(data=data) 

        if self.head is None:
            self.head = new_node 
            return 
        
        current_node = self.head 

        while current_node.next:
            current_node = current_node.next 
        current_node.next = new_node 

    
    def __str__(self):
        res = [] 
        current = self.head 
        while current:
            res.append(current.data) 
            current = current.next 

        return str(res) 




first_list = [1,2,4,7,9,2,1] 
second_list = [1,3,4]

l = LinkedList() 

for i in first_list:
    l.insert_node(i) 



print("Start second list") 


s = LinkedList() 

for i in second_list:
    s.insert_node(i) 



class Solution:
    def MergeTwoSortedList(self, first_list: Node, second_list : Node):
        first_res_data = [] 
        while first_list:
            first_res_data.append(first_list.data) 
            first_list = first_list.next 
        
        second_res_data = [] 
        while second_list:
            second_res_data.append(second_list.data) 
            second_list = second_list.next 
        
        total = first_res_data + second_res_data 
        total.sort() 

        # dummy = Node(0) 
        # current = dummy 
        # for digit in str(total)[::-1]:
        #     current.next = Node(int(digit)) 
        #     current = current.next 

        # return dummy.next 

        dummy = Node(0) 
        current = dummy 

        for data in total:
            current.next = Node(data) 
            current = current.next 
        
        return dummy.next 




        
a = Solution()
x = a.MergeTwoSortedList(l.head, s.head) 

print(x) 

def print_link_list(head):
    res = [] 
    current = head 
    while current:
        res.append(current.data)
        current = current.next 
    return res 

print(f'Data is sorted : {print_link_list(x)}')
        