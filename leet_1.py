class Solution:
    def __init__(self, nums: list[int], target : int):
        self.nums = nums 
        self.target = target 
    
    def TwoSum(self): 
        for i in range(0, len(self.nums) -1 ):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
        return 0 
    

nums = [2,7,11,15]
# nums = [2,5,5,11]

target = 9

s = Solution(nums=nums, target=target) 
print(s.TwoSum()) 