#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        stalls.sort()
        maxPossible = stalls[n - 1] - stalls[0]
        minPossible = stalls[1] - stalls[0]
        for index in range(2, n):
            minPossible = min(minPossible, stalls[index] - stalls[index - 1])
        
        def isPossible(val):
            cowsToBePlaced = k - 1 
            previousCow = 0 
            
            for index in range(1, n):
                diff = stalls[index] - stalls[previousCow] 
                if diff >= val:
                    previousCow = index
                    cowsToBePlaced -= 1
                    if cowsToBePlaced == 0:
                        return True 
            return False

        result = -1 
        left, right = minPossible, maxPossible 
        while left <= right:
            mid = (left + right) // 2 
            if isPossible(mid):
                result = mid 
                left = mid + 1 
            else:
                right = mid - 1
        return result
