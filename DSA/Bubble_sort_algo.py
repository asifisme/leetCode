# Bubble Sort algorithm 
class Bubble_Sort:
    def __init__(self, nums : list[int]):
        self.nums = nums 
    
    def Bubble(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j + 1] < self.nums[j]:
                    self.nums[j + 1] , self.nums[j] = self.nums[j], self.nums[j + 1 ] 
                print(self.nums)
        return self.nums 


# test data 
nums = [10, 5, 2, 8, 7] 
s = Bubble_Sort(nums) 
print(s.Bubble())