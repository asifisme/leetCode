class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        return 

    
    def rotate(self, k):
        if not self.head or k == 0:
            return

        # Find the length of the linked list
        length = 1
        current = self.head
        while current.next:
            current = current.next
            length += 1

        # Make the linked list circular
        current.next = self.head

        # Find the new tail and new head
        k = k % length
        steps_to_new_tail = length - k
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Break the circular linked list
        new_tail.next = None

        # Update the head of the linked list
        self.head = new_head


    def __str__(self):
        res = []
        current = self.head
        while current:
            res.append(current.value)
            current = current.next
        return str(res) 