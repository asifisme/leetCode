class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0 
        l = 0 
        r = len(height) -1 

        while l < r: 
            min_height = min(height[l], height[r]) 
            ans        = max(ans, min_height * (r -l))  

            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1 
        
        return ans 

        

height = [1,8,6,2,5,4,8,3,7] 

s = Solution()
print(s.maxArea(height=height)) 