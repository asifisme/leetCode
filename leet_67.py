class Solutions:
    def __init__(self, a : str, b : str):
        self.a = a 
        self.b = b 
    
    def addBinary(self):
        a = int(self.a, 2)
        b = int(self.b, 2)
        a = bin(a + b )
        
        return a[2:]

a = '11'
b = '1'

test = Solutions(a, b)
print(test.addBinary())