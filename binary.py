
def binary_search(arr: list[int], target: int):
    low = 0
    high = len(arr) -1 

    while low <= high:
        mid = (low + high) // 2 

        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1 


def binary_search_recursion(arr:list[int], target: int, low:int, high:int):
    if low <= high:
        mid = (low + high) // 2 
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            return binary_search_recursion(arr=arr, target=target, low=mid+1, high=high)
        else:
            return binary_search_recursion(arr=arr, target=target, low=low, high=mid-1)
    return -1 


def binary(nums: list[int], target: int)-> int:
    low = 0 
    high = len(nums) -1 

    while low <= high:
        mid = (low + high) // 2 

        if nums[mid] == target:
            return mid  
        elif nums[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1 
    
    # O(log n) 


def linear(nums: list[int], target: int)-> int: 
    for i in range(len(nums)):
        if nums[i] == target:
            return i 
    return -1 

    # O(n) 



def num_sort(nums: list[int]) -> list[int]:
    nums = nums.copy() 
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] <  nums[i]:
                nums[j], nums[i] = nums[i], nums[j] 
    return nums

def bobble_sort(nums: list[int]) -> list[int]:
    n = len(nums) 

    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j] 
    return nums 


arr = [ 2, 3, 4, 10, 40 ]
target = 10 


print(binary_search(arr, target))

print(binary_search_recursion(arr=arr, target=target, low=0, high=len(arr)-1)) 
