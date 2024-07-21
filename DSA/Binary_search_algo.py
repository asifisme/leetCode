# Binary Search Algorithm  
class Binary:
    def __init__(self, nums : list[int], target : int):
        self.nums = nums 
        self.target = target 
    
    def Search(self):
        left = 0 
        right = len(self.nums) -1 
        while left <= right:
            mid = (left + right) // 2 
            if self.nums[mid] == self.target:
                return mid 
            elif self.nums[mid] < self.target:
                left = mid + 1 
            else:
                right = mid - 1 
        return -1 

# test data 
nums = [1,2,3,4,5,6,7,8,10,11] 
target = 8

# call the class 
l = Binary(nums, target)
print(l.Search())