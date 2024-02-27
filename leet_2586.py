def Soluation(word, l, r):
    count = 0 
    v = 'aeiou'
    for i in words[l:r+1]:
        if i[0] in v and i[-1] in v:
            count += 1 
    return count 

words = ["are","amy","u"]
left = 0
right = 2

print(Soluation(words, left, right))
