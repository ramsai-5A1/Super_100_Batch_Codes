class Solution:
    def findAllOnesUsingDFS(self, row, col, grid, n, m):
        if min(row, col) < 0 or row >= n or col >= m or grid[row][col] == 0:
            return 0 

        result = 1 
        grid[row][col] = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for index in range(4):
            newRow = row + dx[index]
            newCol = col + dy[index]
            result += self.findAllOnes(newRow, newCol, grid, n, m)
        return result

    def findAllOnesUsingBFS(self, row, col, grid, n, m):
        Q = [[row, col]]
        result = 1
        grid[row][col] = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while Q:
            curr = Q.pop(0)
            row, col = curr[0], curr[1]
            
            for index in range(4):
                newRow = row + dx[index]
                newCol = col + dy[index]
                if min(newRow, newCol) < 0 or newRow >= n or newCol >= m or grid[newRow][newCol] == 0:
                    continue
                grid[newRow][newCol] = 0
                result += 1
                Q.append([newRow, newCol])
            
        return result
        
        
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0 

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    current = self.findAllOnesUsingBFS(row, col, grid, n, m)
                    result = max(result, current)
        return result            