class Solution(object):
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        result = [[1000000] * n for i in range(m)]
        Q = []
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    Q.append([row, col, 0])
                    result[row][col] = 0

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while Q:
            curr = Q.pop(0)
            row, col = curr[0], curr[1]

            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n and result[newRow][newCol] > curr[2] + 1:
                    result[newRow][newCol] = curr[2] + 1
                    Q.append([newRow, newCol, curr[2] + 1])
        
        return result