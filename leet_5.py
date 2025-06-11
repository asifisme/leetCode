class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [] 
        resLen = 0 

        for i in range(len(s)):
            # ood length 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r -l +1) > resLen: 
                    
        



s = "babad" 

p = Solution()
print(p.longestPalindrome(s))