class Solution:

    #Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        Q = [[KnightPos[0], KnightPos[1], 0]]
        directions = [[-2, 1], [-1, 2],[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
        visited = set()
        visited.add((KnightPos[0], KnightPos[1]))
        while Q:
            curr = Q.pop(0)
            #print(curr)
            row, col, steps = curr[0], curr[1], curr[2]
            if row == TargetPos[0] and col == TargetPos[1]:
                return steps 
                
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
               
                if newRow > 0 and newCol > 0 and newRow <= N and newCol <= N and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    Q.append([newRow, newCol, steps + 1])
        return -1
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
               
              
                
                
            
        
