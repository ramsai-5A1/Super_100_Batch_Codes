class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)

        def recursiveApproach(row, col):
            if row == n - 1:
                return matrix[row][col] 

            result = 0 
            leftDiagnol = 100000000 
            rightDiagnol = 100000000 

            if col - 1 >= 0:
                leftDiagnol = recursiveApproach(row + 1, col - 1)

            if col + 1 < n:
                rightDiagnol = recursiveApproach(row + 1, col + 1)

            belowRow = recursiveApproach(row + 1, col)
            result = min([leftDiagnol, rightDiagnol, belowRow]) + matrix[row][col]
            return result

        cache = [[-1] * n for i in range(n)]

        def memoizationApproach(row, col):
            if row == n - 1:
                return matrix[row][col] 
            elif cache[row][col] != -1:
                return cache[row][col]

            result = 0 
            leftDiagnol = 100000000 
            rightDiagnol = 100000000 

            if col - 1 >= 0:
                leftDiagnol = memoizationApproach(row + 1, col - 1)

            if col + 1 < n:
                rightDiagnol = memoizationApproach(row + 1, col + 1)

            belowRow = memoizationApproach(row + 1, col)
            result = min([leftDiagnol, rightDiagnol, belowRow]) + matrix[row][col]
            cache[row][col] = result 
            return result

        def tabulationApproach():
            cache = [[100000000] * n for i in range(n)]
            for col in range(n):
                cache[n - 1][col] = matrix[n - 1][col]

            for row in range(n - 2, -1, -1):
                for col in range(n - 1, -1, -1):
                    result = 0 
                    leftDiagnol = 100000000 
                    rightDiagnol = 100000000 

                    if col - 1 >= 0:
                        leftDiagnol = cache[row + 1][col - 1]

                    if col + 1 < n:
                        rightDiagnol = cache[row + 1][col + 1]

                    belowRow = cache[row + 1][col]
                    result = min([leftDiagnol, rightDiagnol, belowRow]) + matrix[row][col]
                    cache[row][col] = result 

            result = 10000000 
            for col in range(n):
                result = min(result, cache[0][col])
            return result

        # result = 1000000000
        # for col in range(n):
        #     result = min(result, memoizationApproach(0, col))
        # return result
        return tabulationApproach()
