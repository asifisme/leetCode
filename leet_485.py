class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        res = []
        count = 0 

        for num in nums:
            if num == 1:
                count += 1 
            else:
                res.append(count) 
                count = 0 
            res.append(count)
        return max(res)


nums =  [1,1,0,0,1,1,1,1,0,1]

s = Solution()
print(s.findMaxConsecutiveOnes(nums))