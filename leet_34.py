class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0 
        high = len(nums) - 1 
        first = 0  
        last = 0 
        while low <= high:
            mid = (low + high) // 2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1 
            else:
                high = mid - 1 
                first = mid 
        
        while low <= high:
            mid = (low + high) // 2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1 
            else:
                high = mid - 1 
                last = mid 
        return -1 







nums = [5,7,7,8,8,10]
target = 8 

s = Solution()
print(s.searchRange(nums=nums, target=target))