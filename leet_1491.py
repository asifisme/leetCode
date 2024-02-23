class Soluation:
    def __init__(self, sal: list):
        self.sal = sal 
    
    def averageSalary(self):
        mn = min(self.sal)
        mx = max(self.sal) 
        sm = sum(self.sal) 
        return (sm - mn - mx) / (len(self.sal) - 2)


sal = [8000,9000,2000,3000,6000,1000]

test = Soluation(sal)
print(test.averageSalary())