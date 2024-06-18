class Solution(object):
    def solve(self, board):
        m, n = len(board), len(board[0])
        
        def visitAll(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = '#'
            Q = [[row, col]]
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while Q:
                curr = Q.pop(0)
                for direction in directions:
                    newRow = curr[0] + direction[0]
                    newCol = curr[1] + direction[1]
                    if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n and board[newRow][newCol] == 'O':
                        board[newRow][newCol] = '#'
                        Q.append([newRow, newCol])
        
        for row in range(m):
            visitAll(row, 0)
            visitAll(row, n - 1)
            
        for col in range(n):
            visitAll(0, col)
            visitAll(m - 1, col)
            
        for row in range(m):
            for col in range(n):
                if board[row][col] == '#':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
        