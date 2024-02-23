class Solution:
    def __init__(self, s: str):
        self.s = s  
    def romanToInt(self):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
        n = len(self.s) 
        num = roman_map[self.s[n-1]]
        for i in range(n-2, -1, -1): 
            if roman_map[self.s[i]] >= roman_map[self.s[i+1]]:
                num += roman_map[self.s[i]]
            else:
                num -= roman_map[self.s[i]]
        return num 


s = "LVIII" 
x = Solution(s) 
print(x.romanToInt())