
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



arr = [ 2, 3, 4, 10, 40 ]
target = 10 


print(binary_search(arr, target))

print(binary_search_recursion(arr=arr, target=target, low=0, high=len(arr)-1)) 
