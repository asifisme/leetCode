def Check(s):
    res = ""
    if s is None or len(s) == 0:
        return res 
    else:
        for i in range(0, min([len(x) for x in s])):
            current = s[0][i] 
            for j in range(0, len(s)):
                if s[j][i] != current:
                    return res 
            res += current 
    return res 



s = ["flower","flow","flight"]
print(Check(s))