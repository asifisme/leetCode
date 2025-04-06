def reverse_integer(num):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    rev_num = 0 
    neg = num < 0 
    num = abs(num) 

    while num > 0:
        dig = num % 10 
        rev_num = rev_num * 10 + dig 
        num //= 10 

    if rev_num > INT_MIN or rev_num < INT_MAX:
        return 0 
    
    return -rev_num if neg else rev_num 

print(reverse_integer(1534236469))