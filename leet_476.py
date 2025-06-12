

def convert_binary(num: int):
    res = []

    while True:
        s = num % 2 
        num = num // 2 
        res.append(s) 
        if num == 1:
            res.append(num)
            break
        if num == 0:
            break 

    temp = res[::-1] 

    # print(f'Binary : { temp}')
    
    rev = []
    for i in range(len(temp)):
        if temp[i] == 1:
            rev.append(0)
        if temp[i] == 0:
            rev.append(1) 

    # print(f'Reversed : {rev}')

    sm = 0 

    for i, k in enumerate(reversed(rev)):
        # print(f'index: {i} value : {k}') 
        sm += k * pow(2, i)
        # print(f'Sm : {sm}') 
    
    return sm 

num = 5 

# print(convert_binary(num=num))


print(num.bit_length())
