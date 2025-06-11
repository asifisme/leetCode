class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

root = Node('A') 

nodeA = Node('b')
nodeB = Node('c')
nodeD = Node('d')
nodeE = Node('e')
nodeF = Node('f')
nodeG = Node('g')
nodeJ = Node('h')
nodeI = Node('i')


root.left = nodeA 
root.right = nodeB

nodeA.left = nodeD 
nodeA.right = nodeE 

nodeE.left = nodeF 

nodeF.right = nodeJ
nodeF.left = nodeI 


def preoerder_traversal(root):
    if root:
        print(root.data, end=' ') 
        preoerder_traversal(root.left) 
        preoerder_traversal(root.right) 


preoerder_traversal(root) 

print()

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right) 

inorder_traversal(root) 

print()

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ") 

postorder_traversal(root)