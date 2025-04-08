class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # for i in range(k-1):
        #     n = max(nums)
        #     nums.remove(n) 
        
        # return max(nums) 
        # Above solution coutht Runtime error 
        nums = sorted(nums, reverse=True)
        return nums[k-1]



nums =  [3,2,3,1,2,4,5,5,6]
k = 4

s = Solution()
print(s.findKthLargest(nums=nums, k=k))