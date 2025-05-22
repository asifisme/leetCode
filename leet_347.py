class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1 
            else:
                num_map[num] += 1 

        res = []
        count = 0 
        for val in num_map.keys():
            res.append(val) 
            count += 1 
            if count == k:
                return res 




nums = [1,1,1,2,2,3]
k = 2

s = Solution()
print(s.topKFrequent(nums=nums, k=k)) 