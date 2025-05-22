class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i) 
                    res.append(j) 
        return res 


nums = [3,2,4] #[2,7,11,15]

target = 6

s = Solution()
print(s.twoSum(nums=nums, target=target))