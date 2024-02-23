# leetCode 14 longest common prefix 
class Solution:
    def __init__(self, s : list[str]):
        self.s = s 
    
    def Prefix(self):
        res = "" 
        if self.s is None or len(self.s) == 0:
            return res 
        else:
            for i in range(0, min([len(x) for x in self.s])):
                current = self.s[0][i] 
                for j in range(0, len(self.s)):
                    if self.s[j][i] != current:
                        return res 
                res += current 
        return res 
            
strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
x = Solution(strs)
print(x.Prefix())