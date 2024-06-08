class Solution:
    def findPath(self, m, n):
        result = []
        
        def solveIt(row, col, path):
            if min(row, col) < 0 or max(row, col) >= n or m[row][col] == 0:
                return
            elif row == n - 1 and col == n - 1:
                result.append("".join(path))
                return 
            
            m[row][col] = 0
            
            path.append("U")
            solveIt(row - 1, col, path)
            path.pop()
            
            path.append("D")
            solveIt(row + 1, col, path)
            path.pop()
            
            path.append("L")
            solveIt(row, col - 1, path)
            path.pop()
            
            path.append("R")
            solveIt(row, col + 1, path)
            path.pop()
            
            m[row][col] = 1 
            
        path = []
        solveIt(0, 0, path)
        return result
