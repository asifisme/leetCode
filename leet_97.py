
def InterleavingString(first_str : str, second_str : str, third_str : str):

    res = list(third_str)
    count = 0
    for i, v in enumerate(first_str):
        if v in res:
            res.remove(v)
            count += 1 

    res_s = list(third_str)
    count_s = 0 
    
    for i, v in enumerate(second_str):
        if v in res_s:
            res_s.remove(v) 
            count_s += 1 
    
    return (count == len(first_str)) and  (count_s == len(second_str))
    






s1 = "aabcc"
# s1 = 'xxf'
s2 = "dbbca"
s3 = "aadbbbaccc"  # "aadbbcbcac"

print(InterleavingString(s1, s2, s3))