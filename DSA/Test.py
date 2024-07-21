# select sort algorithm 
class Selection_Sort:
    def __init__(self, nums : list[int]):
        self.nums = nums 
    
    def Select(self):
        for i in range(len(self.nums) - 1):
            min_index = i 
            for j in range(i + 1, len(self.nums)):
                if self.nums[j] < self.nums[min_index]:
                    min_index = j 
                
                # swap the value 
                if i != min_index:
                    self.nums[i], self.nums[min_index] = self.nums[min_index], self.nums[i]
        return self.nums 

 
nums = [10, 5, 2, 8, 7] 
s = Selection_Sort(nums) 
print(s.Select())