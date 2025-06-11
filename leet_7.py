class Solution:
    def reverse(self, x: int) -> int:
        prev = 0 
        x = abs(x)
        while x > 0: 
           s = x // 10 
           c = x % 10 
           prev = prev * 10 + c 
           x //= 10 

        return prev 


s = Solution() 
print(s.reverse(-123))