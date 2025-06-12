class Solution:
    def plusOne(self, digits: list[int])-> list[int]:
        # first soluation 
        # for i in range(len(digits)-1, -1, -1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits 
        #     digits[i] = 0 
        # return [1] + digits

        # second soluation 
        res = ''
        for i in (digits):
            res += str(i) 
        
        res = int(res) + 1 

        return [int(i) for i in str(res)]
        

       

digits = [9, 9]


s = Solution()

print(s.plusOne(digits=digits))
        
