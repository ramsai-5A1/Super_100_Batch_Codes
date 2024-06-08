class Solution:
    
    
    def minimizeCost(self, height, n, k):
        cache = [-1] * n
        def solveIt(index):
            if index == n - 1:
                return 0 
            elif cache[index] != -1:
                return cache[index]
                
            result = 100000000 
            for i in range(1, k + 1):
                nextIndex = index + i 
                if nextIndex >= n:
                    break 
                currCost = abs(height[index] - height[nextIndex]) + solveIt(nextIndex)
                result = min(result, currCost)
            cache[index] = result
            return result
            
        def solveItUsingTabulation():
            cache[n - 1] = 0 
            for index in range(n - 2, -1, -1):
                result = 100000000 
                for i in range(1, k + 1):
                    nextIndex = index + i 
                    if nextIndex >= n:
                        break 
                    currCost = abs(height[index] - height[nextIndex]) + cache[nextIndex]
                    result = min(result, currCost)
                cache[index] = result
            return cache[0]
            
            
        return solveItUsingTabulation()
            
