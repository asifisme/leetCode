
def RemoveDuplicate(nums):
    count = 0 

    for num in nums:
        if count < 1 or num > nums[count - 1]:
            nums[count] = num 
            count += 1 
    return count 

nums = [0,0,1,1,1,2,2,3,3,4]

print(RemoveDuplicate(nums)) 