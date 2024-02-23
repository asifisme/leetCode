class Soluation: 
    def __init__(self, nums : list, target  : int):
        self.nums = nums 
        self.target = target 
    
    def Binary(self):
        left, right = 0, len(self.nums) - 1 
        while left <= right:
            mid = (left + right) // 2 
            if self.target == self.nums[mid]:
                return mid 
            elif self.target > self.nums[mid]:
                left = mid + 1 
            else:
                right = mid + 1 
        
        return left 
    

nums = [1,3,5,6]
target = 6

test = Soluation(nums, target) 
print(test.Binary())