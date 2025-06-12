class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:        
        res = ''
        for char in reversed(s):
            if char == '-':
                continue 
            res += char 

        res = res[::-1]

        r = ''
        n = len(res) 
        count = 0 
        tcount = 0 
        res = [c for c in res] 
        while True:
            count += 1 
            if not res:
                break 
            x = res.pop() 
            
            if count == k:
                count = 0 
                if res:
                    r += x + '-' 
                else:
                    r += x 
                continue 
            r += x 
        
        return r[::-1].upper()

            
            
s = "5F3Z-2e-9-w"
k = 4

# s = "2-5g-3-J"
# k = 2

x = Solution()
print(x.licenseKeyFormatting(s=s, k=k)) 