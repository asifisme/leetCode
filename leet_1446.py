class Solution:
    def maxPower(self, s: str) -> int:
        res = []        
        for i in range(len(s)):
            count = 0 
            for j in range(i, len(s)-1):
                if s[j] == s[j+1]:
                    count +=1 
                else:
                    break 
            res.append(count)

            
            
        return max(res) + 1 


s = "leetcode"
a = Solution()
print(a.maxPower(s)) 