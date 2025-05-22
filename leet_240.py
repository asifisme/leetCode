class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        low = 0 
        hight = len(matrix[0]) -1 

        while low <= hight:
            mid = (low + hight) // 2 

            if matrix[low][mid] == target:
                return True 
            elif matrix[low][mid] < target:
                low = mid + 1 
            else:
                hight = mid - 1 
        return False 


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5

s = Solution()

print(s.searchMatrix(matrix=matrix, target=target))
