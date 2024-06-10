class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)

        def recursiveApproach(row, col):
            if row == n or col < 0 or col >= n:
                return 0 

            choice1 = recursiveApproach(row + 1, col)
            choice2 = recursiveApproach(row + 1, col + 1)
            return min(choice1, choice2) + triangle[row][col]
             

        cache = [[0] * (n + 1) for i in range(n + 1)]
        def memoizationApproach(row, col):
            if row == n or col < 0 or col >= n:
                return 0 
            elif cache[row][col] != -1:
                return cache[row][col]

            choice1 = memoizationApproach(row + 1, col)
            choice2 = memoizationApproach(row + 1, col + 1)
            cache[row][col] = min(choice1, choice2) + triangle[row][col] 
            return cache[row][col]

        def tabulationApproach():
            for row in range(n - 1, -1, -1):
                for col in range(n - 1, -1, -1):
                    if col >= len(triangle[row]):
                        continue
                    choice1 = cache[row + 1][col]
                    choice2 = cache[row + 1][col + 1]
                    cache[row][col] = min(choice1, choice2) + triangle[row][col] 
            return cache[0][0]
             

        return tabulationApproach()
