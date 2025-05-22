
class Soluation:
    def SpiralMaxrix(self, nums: list[int]):
        res = []

        for i, item in enumerate(nums):
            if i == 0:
                for j in item:
                    res.append(j)
            if i == 1:
                res.append(res[-1][-1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]

s = Soluation()
print(s.SpiralMaxrix(matrix))