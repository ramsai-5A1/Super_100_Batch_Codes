class Solution(object):
    def searchMatrix(self, matrix, target):
        n, m = len(matrix), len(matrix[0])
        left, right = 0, (n * m) - 1
        while left <= right:
            mid = (left + right) // 2 
            row = mid // m 
            col = mid % m 
            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] > target:
                right = mid - 1 
            else:
                left = mid + 1 
        return False
