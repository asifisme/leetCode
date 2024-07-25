# inseration Sort 
class Inseration_Sort:
    def __init__(self, nums : list[int]):
        self.nums = nums 
    
    def Inseration(self):
        for i in range(len(self.nums)):
            items = self.nums[i] 
            j = i - 1 
            while j >= 0 and self.nums[j] > items:
                self.nums[j + 1] = self.nums[j] 
                j = j - 1
            self.nums[j + 1] = items 
        
        return self.nums 


# Test data 
nums = [8, 2, 8, 7,1,3,5,6] 
I = Inseration_Sort(nums) 
print(I.Inseration())