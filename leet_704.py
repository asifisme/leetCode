class Solution:
    def __init__(self, nums : list , target : int ):
        self.nums = nums 
        self.target = target 
    
    def Search(self):
        left = 0 
        right = len(self.nums) - 1 

        while left <= right:
            mid = ( left + right ) // 2 
            if self.nums[mid] == self.target:
                return mid 
            elif self.target > self.nums[mid]: 
                left = mid + 1 
            else:
                right = mid - 1 
        else:
            return -1 



nums = [-1,0,3,5,9,12]
target = 2

s = Solution(nums, target) 

print(s.Search())