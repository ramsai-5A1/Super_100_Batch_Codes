class Solution(object):
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        result = 0 

        def visitAllOnes(row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            visitAllOnes(row - 1, col)
            visitAllOnes(row + 1, col)
            visitAllOnes(row, col - 1)
            visitAllOnes(row, col + 1)
            

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    visitAllOnes(row, col)
                    result += 1

        return result
        