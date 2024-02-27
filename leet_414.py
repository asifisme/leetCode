def Soluation(nums): 
    res = list(set(nums))
    res.sort()
    print(res)
    if len(res) <= 2:
        return max(res) 
    else:
        return res[-3]


# nums = [2,2,3,1,5,6,7,4,6,8,10
nums  = [-1,2,3]
print(Soluation(nums=nums))
