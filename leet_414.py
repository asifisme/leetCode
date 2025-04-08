class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # if len(nums) <= 2:
        #     return max(nums) 
        # else:
        #     nm = list(set(nums)) 
        #     nm.remove(max(nm))
        #     nm.remove(max(nm))
        #     return max(nm)
        nums = list(set(nums))
        nums = sorted(nums, reverse= True)
        return nums[2] if len(nums) <=2 else nums[0]

nums = [2,2,3,1] 

s = Solution()
print(s.thirdMax(nums))