class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = [] 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-4):
                pass 



nums = [1,0,-1,0,-2,2]
target = 0

s = Solution()
print(s.fourSum(nums=nums, target=target))
