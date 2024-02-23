class Soluations:
    def __init__(self, nums : list):
        self.nums = nums 
    
    def plusOne(self):
        for i,d in reversed(list(enumerate(self.nums))): 
            if d < 9:
                self.nums[i] += 1 
                return self.nums
            self.nums[i] = 0 

        return [1] + self.nums 


nums = [9,9]

test = Soluations(nums)
print(test.plusOne())