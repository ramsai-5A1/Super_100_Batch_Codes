class NumMatrix(object):

    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for i in range(m)]
        
        for row in range(m):
            for col in range(n):
                cache[row][col] = matrix[row][col]
                if row > 0:
                    cache[row][col] += cache[row - 1][col]
                if col > 0:
                    cache[row][col] += cache[row][col - 1]
                if row > 0 and col > 0:
                    cache[row][col] -= cache[row - 1][col - 1]
                    
                    
        self.cache = cache
        
        

    def sumRegion(self, row1, col1, row2, col2):
        # big sum 
        bigSum = self.cache[row2][col2]
        
        # upper rectangle sum 
        upperSum = 0 
        if row1 > 0:
            upperSum = self.cache[row1 - 1][col2]
        
        # left rectangle sum 
        leftSum = 0 
        if col1 > 0:
            leftSum = self.cache[row2][col1 - 1]
        
        # commom rectangle sum 
        commonSum = 0 
        if row1 > 0 and col1 > 0:
            commonSum = self.cache[row1 - 1][col1 - 1]
            
        result = bigSum - upperSum - leftSum + commonSum 
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)