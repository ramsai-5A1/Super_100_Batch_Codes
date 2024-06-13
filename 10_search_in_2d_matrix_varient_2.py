class Solution(object):
    def searchMatrix(self, matrix, target):
        i, j = 0, len(matrix[0]) - 1 
        while i >= 0 and j >= 0 and i < len(matrix):
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                j -= 1 
            else:
                i += 1 
        return False
        
