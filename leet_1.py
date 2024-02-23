class Soluations: 
    def __init__(self, nums : list, target : int):
        self.nums = nums 
        self.target = target 
    
    def tSum(self):
        for i in range(len(self.nums)):
            x = self.target - self.nums[i]
            for j in range(i+1, len(self.nums)):
                if x == self.nums[j]:
                    return [i, j]
            

nums = [3,3]
target = 6

test = Soluations(nums, target)

print(test.tSum())

# Solved code 