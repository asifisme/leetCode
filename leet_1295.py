class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0 
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1 
        return count 



nums = [555,901,482,1771]
s = Solution()
print((s.findNumbers(nums)))