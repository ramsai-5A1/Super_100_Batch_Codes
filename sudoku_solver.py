class Solution(object):
    def isPossible(self, board, x, y, value):
            # Same row checking 
            for col in range(9):
                if board[x][col] == str(value):
                    return False
            
            # Same col checking
            for row in range(9):
                if board[row][y] == str(value):
                    return False
            
            # Same 3 * 3 matrix checking 
            topRow = (x // 3) * 3 
            topCol = (y // 3) * 3 
            
            for i in range(3):
                for j in range(3):
                    if board[topRow + i][topCol + j] == str(value):
                        return False
            return True

    def solveThis(self, x, y, board):
        #print(x, y, board)
        if x == 9:
            return True
    
        nextX, nextY = -1, -1 
        
        if y == 8:
            nextX = x + 1 
            nextY = 0 
        else:
            nextX = x 
            nextY = y + 1
            
        if board[x][y] != ".":
            return self.solveThis(nextX, nextY, board)
            
            
        for value in range(1, 10):
            if self.isPossible(board, x, y, value) == True:
                board[x][y] = str(value)
                result = self.solveThis(nextX, nextY, board)
                if result == True:
                    return True
                board[x][y] = "."
                    
        return False

    def solveSudoku(self, board):
        self.solveThis(0, 0, board)
