# leetcode problem 350 intersection of two arrays 

class Solution:
    def __init__(self, nums_one : list[int], nums_two : list[int]):
        self.nums_one = nums_one 
        self.nums_tow = nums_two 
    
    def intersection(self):
        dic_one = {} 
        dic_two = {} 

        for i in self.nums_one:
            if i in dic_one:
                dic_one[i] += 1 
            else:
                dic_one[i] = 1 


        for i in self.nums_tow:
            if i in dic_two:
                dic_two[i] += 1 
            else:
                dic_two[i] = 1 

        res = [] 

        for key in dic_one:
            if key in dic_two:
                min_count = min(dic_one[key], dic_two[key]) 
                res.extend([key] * min_count) 
        return res 

if __name__ == "__main__":
    nums1 = [1,2,2,1] 
    nums2 = [2,2]
    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]

    s = Solution(nums1, nums2) 
    print(s.intersection())