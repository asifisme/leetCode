class Soluations:
    def __init__(self, txt : str):
        self.txt  = txt 
    
    def lastWord(self):
        x = self.txt.split()
        x = len(x[-1])
        return x 


txt = "Hello world"

test = Soluations(txt)
print(test.lastWord())