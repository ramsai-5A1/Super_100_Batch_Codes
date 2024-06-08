class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        def recursiveApproach(row, col):
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            elif row == m or col == n:
                return 10000000 
            
            bottomDirection = recursiveApproach(row + 1, col)
            rightDirection = recursiveApproach(row, col + 1)
            result = min(bottomDirection, rightDirection) + grid[row][col] 
            return result

        cache = []
        for i in range(m):
            row = [-1] * n 
            cache.append(row)

        def memoizationApproach(row, col):
            if row == m - 1 and col == n - 1:
                return grid[row][col]
            elif row == m or col == n:
                return 10000000 
            elif cache[row][col] != -1:
                return cache[row][col]
            
            bottomDirection = memoizationApproach(row + 1, col)
            rightDirection = memoizationApproach(row, col + 1)
            result = min(bottomDirection, rightDirection) + grid[row][col] 
            cache[row][col] = result
            return result 

        def tabulationApproach():
            cache = []
            for i in range(m + 1):
                row = [10000000] * (n + 1)
                cache.append(row)
            cache[m - 1][n - 1] = grid[m - 1][n - 1]

            for row in range(m - 1, -1, -1):
                for col in range(n - 1, -1, -1):
                    if row == m - 1 and col == n - 1:
                        continue 

                    bottomDirection = cache[row + 1][col]
                    rightDirection = cache[row][col + 1]
                    result = min(bottomDirection, rightDirection) + grid[row][col] 
                    cache[row][col] = result
            return cache[0][0]


            

        return tabulationApproach()
        
