class Solution:
    def minTime (self, arr, n, k):
        # if the 'k' matches with 'n', then each painter can paint one board
        minPossibleTime = max(arr)
        
        # if there is one painter avaibale, then he takes the below amount of time to complete
        maxPossibleTime = sum(arr)
        
        def isPossible(value):
            paintersCount = 1 
            currSum = 0 
            for ele in arr:
                if ele > value:
                    return False 
                elif currSum + ele > value:
                    currSum = ele 
                    paintersCount += 1 
                    if paintersCount > k:
                        return False 
                else:
                    currSum += ele 
            return True
        
        left, right = minPossibleTime, maxPossibleTime
        result = -1
        while left <= right:
            mid = (left + right) // 2 
            if isPossible(mid):
                result = mid 
                # Since we need to find minimum time, so reducing further
                right = mid - 1 
            else:
                left = mid + 1 
        return result
