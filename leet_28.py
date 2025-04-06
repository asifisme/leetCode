def Answer(haystack : str, needle : str):
    for s in range(len(haystack)):
        count = 0
        res = []
        c = 0 
        for i in range(s, len(haystack)):
            c += 1 
            if haystack[i] == needle[count]:
                res.append(haystack[i]) 
                count += 1 
            else:
                break 
            if len(needle) == c:
                break 
        if ''.join(res) == needle:
            return s
    return -1 





haystack = "hello"

needle = "ll"



print(Answer(haystack, needle))