class Solution:
    def __init__(self, nums: list[int], k : int):
        self.nums = nums 
        self.k = k 
    def Operation(self):
        seen = set() 
        for i, num in enumerate(reversed(self.nums)):
            if num > self.k:
                continue 
            seen.add(num) 
            if len(seen) == k:
                print(seen)
                return i + 1 
# nums = [3,1,5,4,2]
# k = 5
nums = [3,2,5,3,1]
k = 3
x = Solution(nums, k)
print(x.Operation())