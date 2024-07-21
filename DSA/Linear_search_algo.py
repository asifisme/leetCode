# linear search algorithm 

class Linear:
    def __init__(self, nums : list[int], target : int): 
        self.nums = nums 
        self.target = target 
    
    # search functions 
    def Search(self):
        for i in range(len(self.nums)):
            if self.nums[i] == self.target:
                return i 
        return -1 

        """ Create a hash map for short listing keys and values """
        # res = {} 
        # for i in self.nums:
        #     if i not in res:
        #         res[i] = 1 
        #     else:
        #         res[i] += 1 
        
        # for i in list(res):
        #     if self.target == i:
        #         return res[i] 
        # return -1 


# test data 
nums = [5,5,5,3,3,5,1,5,9,7,8,1,10,1,13,18,10,10]
target = 10 

l = Linear(nums, target) 
print(l.Search())