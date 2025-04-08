
# def Solution(nums: list[int]):
#     for i in range(len(nums)-1):
#         min_index = i 
#         for j in range(len(nums)):
#             if nums[j] < nums[min_index]:
#                 min_index = j 
#         if i != min_index:
#             nums[i], nums[min_index] = nums[min_index], nums[i] 
    
#     return nums[0]



# nums = [4,5,6,7,0,1,2] 

# print(Solution(nums))


def findMin( nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums

nums = [4,5,6,7,0,1,2] 
x =findMin(nums) 
print(x)