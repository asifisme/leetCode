

class Solution:
    def rotate(self, nums: int, k: int) -> None:

        for i in range(k):
           last = nums.pop()
           nums.insert(0, last)
        return nums 
       
     
        
nums = [1,2,3,4,5,6,7]

s = Solution() 
print(s.rotate(nums, 3)) 