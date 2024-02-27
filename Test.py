res = []
def permutation(s, i=0):
    if i == len(s):
        x = str(''.join(s))
        res.append([x])
    for j in range(i, len(s)):
        words = [c for c in s] 
        words[i], words[j] = words[j], words[i] 
        permutation(words, i+1) 
    return res 

s = 'just' 
print(permutation(s))

