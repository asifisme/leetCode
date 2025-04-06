class Soluation:
    def Length(self, s : str):
        count = 0 
        prev = " "
        for char in s:
            if char != " ":
                if prev == " ":
                    count = 1 
                else:
                    count += 1 
            prev = char 
        return count 
            
        
text = "   fly me   to   the moon  "  #"Today is a nice day"

s = Soluation()
print(s.Length(text))