# select sort algorithm 
class Sort_Algorithm:
    def __init__(self, nums : list[int]):
        self.nums = nums 
    # Bubble Sort Algorithm 
    def Bubble_Sort(self):
        count = 0 
        for i in range(len(self.nums)):
            for j in range(len(self.nums) - i - 1):
                count += 1 
                if self.nums[j + 1]  < self.nums[j]:
                    self.nums[j], self.nums[j + 1] = self.nums[j + 1], self.nums[j] 
        return [self.nums , count]
    
    # selection sort Algorithm 
    def Selection_Sort(self):
        count = 0 
        for i in range(len(self.nums) - 1 ):
            index_min = i
            for j in range(i + 1, len(self.nums) ):
                count += 1 
                if self.nums[j] < self.nums[index_min]:
                    index_min = j 
                if index_min != i:
                    self.nums[j], self.nums[index_min] = self.nums[index_min], self.nums[j] 
        return [self.nums, count ]
    
    

        
 
nums = [10, 5, 2, 8, 7,1,3,5,6] 
s = Sort_Algorithm(nums) 
print(s.Bubble_Sort())
print(s.Selection_Sort())