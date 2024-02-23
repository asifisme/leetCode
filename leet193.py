class Soluations: 
    def __init__(self, phn):
        self.phn = open(phn, 'r') 

    def check(self):
        res = []
        row = self.phn.readlines()
        for i in row: 
            res.append(str(i))
        print(res, end="")

            

x = Soluations('phn_num.txt')

x.check()