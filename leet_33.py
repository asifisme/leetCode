
def Search(nums : list[int], target : int):
    low = 0 
    high = len(nums) 
    while low <= high:
        mid = (low + high) // 2 

        if nums[mid] == target:
            return mid 
        elif target < nums[low]:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1 





nums = [4,5,6,7,0,1,2]

target = 0

print(Search(nums, target))