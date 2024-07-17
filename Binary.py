# Binary Search 
class Search:
    def __init__(self, nums : list[int], target : int ):
        self.nums = nums 
        self.target = target 
    
    def Binary(self):
        left = 0 
        right = len(nums) - 1 
        # Take a while loop 
        while left <= right:
            mid = ( left + right) // 2 

            # check targeted of mid index 
            if self.nums[mid] == self.target:
                return mid 
            elif self.nums[mid] < self.target:
                left = mid + 1 
            else:
                right = mid - 1 
        return -1 


# test data  
nums = [1,2,3,4,5,6,7,8,9]
target = 10 

# call class binary search alghrothm 

b = Search(nums=nums, target=target) 

print(b.Binary()) # print index number of the targeted value of list 