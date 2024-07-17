# Account Balance after Rounded purchase 
class Solution:
    def __init__(self, num : int):
        self.num = num 
    
    def Rounded_purchase(self):
        r = 0 
        if self.num >= 0 and self.num <= 100:
            if self.num == 0:
                return 100 - 10 
            elif self.num <= 9:
                r = self.num 
                while True:
                    r += 1 
                    if r // 5 == 2:
                        return 100 - r 

            elif self.num >= 10:
                if self.num % 5 == 0:
                    r = self.num + 1 
                    while True:
                        r += 1 
                        if r % 5 == 0:
                            return 100 - r 
                else:
                    r = self.num 
                    while True:
                        r += 1 
                        if r % 5 == 0:
                            return 100 - r 
        return 0 


# other solutions         return 100 - (self.num + 5) // 10 * 10

num = int(input("Input test case :) "))

p = Solution(num) 
print(p.Rounded_purchase())
