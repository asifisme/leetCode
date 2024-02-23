class Solutions:
    def __init__(self, num1: str, num2: str):
        self.num1 = num1 
        self.num2 = num2 
    
    def strMul(self):
        return (int(self.num1) * int(self.num2))


num1 = '123'
num2 = '456'

test = Solutions(num1, num2)
print(test.strMul())