class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        num_map = {} 
        for num in nums:
            if num not in num_map:
                num_map[num] = 1 
            else:
                num_map[num] += 1 
        
        for key, val in num_map.items():
            if val == max(num_map.values()):
                return key 

        


nums = [3,2,3] #[2,2,1,1,1,2,2] 

s = Solution()
print(s.majorityElement(nums=nums))