
def linear_search(arr: list[int], target: int):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 


def linear_search_recursive(arr: list[int], target: int, index: int = 0):
    if index == len(arr):
        return -1 
    
    if arr[index] == target:
        return index 
    
    return linear_search_recursive(arr, target, index + 1) 


arr = [10, 23, 45, 70, 11, 15]
target = 70 

print(linear_search(arr=arr, target=target)) 

print(linear_search_recursive(arr, target)) 
