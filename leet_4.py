class Solution:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1 
        self.nums2 = nums2 
    
    def Median(self):
        x = self.nums1 + self.nums2 
        x.sort()
        l,r = 0, len(x)
        mid = (l + r) // 2 
        print(mid)
        return (sum(x) / len(x))

nums1 = [1,2]
nums2 = [3,4,5]

test = Solution(nums1, nums2) 

print(test.Median())