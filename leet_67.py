class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1] 
    
        if not len(a) == len(b):
            if len(a) < len(b):
                a = a + '0' * (len(b) - len(a))
            if len(b) < len(a):
                b = b + '0' * (len(a) - len(b)) 
        
        res = ''
        carr = '0'

        for i in range(len(a)):
            if a[i] == '0' and b[i] == '0':
                if carr == '1':
                    res += '1' 
                    carr = '0'
                else:
                    res += '0'
            if (a[i] == '1' and b[i] == '0') or (a[i] == '0' and b[i] == '1') :
                if carr == '1':
                    res += '0'
                    carr = '1'
                else:
                    res += '1'  
            if a[i] == '1' and b[i] == '1':
                if carr == '1':
                    res += '1' 
                else:
                    res += '0'
                carr = '1'
        
        if carr == '1':
            res += '1'
        
        return res[::-1]

            




a = "1010"
b = "1011"

s = Solution()
print(s.addBinary(a, b))