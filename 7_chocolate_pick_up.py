class Solution:
    def solve(self, n, m, grid):
        def recursiveApproach(row, col1, col2):
            if row == n or min(col1, col2) < 0 or max(col1, col2) >= m:
                return 0 
                
            currResult = grid[row][col1]
            if col1 != col2:
                currResult += grid[row][col2]
                
            old1 = grid[row][col1]
            old2 = grid[row][col2]
                
            grid[row][col1] = 0
            grid[row][col2] = 0
            
            nextResult = 0
            directions = [-1, 0, 1]
            for index1 in range(3):
                for index2 in range(3):
                    newCol1 = col1 + directions[index1]
                    newCol2 = col2 + directions[index2]
                    nextResult = max(nextResult, recursiveApproach(row + 1, newCol1, newCol2))
                
            
            grid[row][col1] = old1 
            grid[row][col2] = old2
            
            
            return currResult + nextResult
        
        
        cache = []
        for i in range(n):
            row = []
            for j in range(m):
                col = []
                for k in range(m):
                    col.append(0)
                row.append(col)
            cache.append(row)
                    
    
        
        def memoizationApproach(row, col1, col2):
            if row == n or min(col1, col2) < 0 or max(col1, col2) >= m:
                return 0 
            elif cache[row][col1][col2] != -1:
                return cache[row][col1][col2]
                
            currResult = grid[row][col1]
            if col1 != col2:
                currResult += grid[row][col2]
                
            old1 = grid[row][col1]
            old2 = grid[row][col2]
                
            grid[row][col1] = 0
            grid[row][col2] = 0
            
            nextResult = 0
            directions = [-1, 0, 1]
            for index1 in range(3):
                for index2 in range(3):
                    newCol1 = col1 + directions[index1]
                    newCol2 = col2 + directions[index2]
                    nextResult = max(nextResult, memoizationApproach(row + 1, newCol1, newCol2))
                
            
            grid[row][col1] = old1 
            grid[row][col2] = old2
            
            
            cache[row][col1][col2] = currResult + nextResult 
            return cache[row][col1][col2]
        
        def tabulationApproach():
            for col1 in range(m):
                for col2 in range(m):
                    cache[n - 1][col1][col2] = grid[n - 1][col1]
                    if col1 != col2:
                        cache[n - 1][col1][col2] += grid[n - 1][col2]
                        
                        
            for row in range(n - 2, -1, -1):
                for col1 in range(m):
                    for col2 in range(m - 1, -1, -1):
                        currResult = grid[row][col1]
                        if col1 != col2:
                            currResult += grid[row][col2]
                            
                        
                        nextResult = 0
                        directions = [-1, 0, 1]
                        for index1 in range(3):
                            for index2 in range(3):
                                newCol1 = col1 + directions[index1]
                                newCol2 = col2 + directions[index2]
                                if min(newCol1, newCol2) < 0 or max(newCol1, newCol2) >= m:
                                    continue
                                
                                nextResult = max(nextResult, cache[row + 1][newCol1][newCol2])
                            
                        
                        
                        cache[row][col1][col2] = currResult + nextResult 
            return cache[0][0][m - 1]
        
        return tabulationApproach()
