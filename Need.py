def isPalindrome(s):
    return s == s[::-1]

def isPal(str):
    for i in range(0, len(str)//2): 
        if str[i] != str(len(str) - i - 1):
            return False 
    return True  

def MinimumLength(nums: list):
    return min([len(x) for x in nums])

def MaximumLength(nums: list):
    return max([len(i) for i in nums])
