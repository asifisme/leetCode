def Duplicate(nums):
    hashmap = dict() 
    for i in range(len(nums)):
        if nums[i] in hashmap.keys():
            return True 
        else:
            hashmap[nums[i]] = i 
    return False 


nums = [-24500,-24499,-24498,-24497,-24496,-24495,-24494,-24493]
print(Duplicate(nums))
