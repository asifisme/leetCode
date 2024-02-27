def Soluation(nums):
    if len(nums) <= 2:
        return -1 
    else:
        m = max(nums)
        n = min(nums) 
        res = [] 
        for i in nums:
            if i == m or i == n:
                continue 
            else:
                res.append(i) 
        return res[0]

nums = [2,4,25]
print(Soluation(nums))