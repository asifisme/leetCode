class Soluation:
    def __init__(self, nums : int):
        self.nums = nums 
    
    def isPal(self):
        rev = 0 
        x = self.nums 

        if x < 0:
            return False 
        
        while x != 0:
            rev = (rev * 10) + (x % 10)
            x = x // 10 
            
        if self.nums == rev:
            return True
        
nums = 121
test = Soluation(nums)

print(test.isPal())
# Solved Code 