def Range(nums): 
    l = len(nums) 
    for i in range(l-2, -1, -1):
        print(f'index : {i} and value : {nums[i]}') 

nums = [1,2,3,4,5,6,7,8,9]
Range(nums)