class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() 
        longest = 0 
        l = 0
        for i in range(len(s)):
            while s[i] in char_set:
               char_set.remove(s[l]) 
               l += 1 

            longest = max(longest, (i - l)+1 )
            char_set.add(s[i]) 
            
        return longest 
      
        
            
s = "pwwkew" 

call = Solution()
print(call.lengthOfLongestSubstring(s)) 

