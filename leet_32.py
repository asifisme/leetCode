def LongestValid(s: str):
    # count = 0 
    # for i in range(len(s)-1):
    #     if s[i] == '(' and s[i+1] == ')':
    #         count += 2 
    # return count  # pass 64 test case 

    stack = [-1]
    max_length = 0 

    for i, v in enumerate(s):
        if v == '(':
            stack.append(i) 
        else:
            stack.pop() 

            if not stack:
                stack.append(i) 
            else:
                max_length = max()


s = ")()())"

print(LongestValid(s))