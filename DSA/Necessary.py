# all every things 
class Search:
    def __init__(self, nums : list[int], target : int):
        self.nums = nums 
        self.target = target 
    
    # Linear Seach Algorithms 
    def Linear(self):
        for i in range(len(self.nums)):
            if self.nums[i] == self.target:
                return i 
        return -1 
    
    # Binary Search Algorithm 
    def Binary(self):
        left = 0 
        right = len(self.nums) - 1 

        while left <= right:
            mid = ( left + right) // 2 
            if self.nums[mid] == self.target:
                return mid 
            elif self.nums[mid] < self.target:
                left = mid + 1 
            else:
                right = mid - 1 
        return -1 

# Sorting algorithm 
class Sorting_algorithm:
    def __init__(self, nums : list[int]):
        self.nums = nums 
    
    # selection sorting algorithm 
    def Selection(self):
        for i in range(len(self.nums) - 1 ):
            index_min = i 
            for j in range(i+1, len(self.nums)):
                if self.nums[j] < self.nums[index_min]:
                    index_min = j 
                
                # check and swaping 
                if i != index_min:
                    self.nums[i], self.nums[index_min] = self.nums[index_min], self.nums[i] 
        # finally return sorted values 
        return self.nums
    
    # Bubble Sort algorithm 
    def Bubble_sort(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j + 1] < self.nums[j]:
                    self.nums[j], self.nums[ j + 1] = self.nums[j + 1], self.nums[j] 
        return self.nums 





# # Test data 
# nums = [1,3,4,7,11,99,177]
# target = 4


# # first call 
# s = Search(nums, target) 
# print(s.Linear())

# # second call 
# p = Search(nums, target) 
# print(p.Binary())



# Sorting algorithm 
nums = [5,3,1,4,3,7,6] 

s = Sorting_algorithm(nums) 
print(s.Selection())
print(s.Bubble_sort())