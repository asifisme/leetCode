def Valided(s : str):
    stactk = [] 
    for c in s:
        if c == '(':
            stactk.append(')') 
        elif c == '{':
            stactk.append('}') 
        elif c == '[':
            stactk.append(']') 
        elif not stactk or stactk.pop() != c:
            return False 
    return not stactk 
        

s = "()]{}"

print(Valided(s))