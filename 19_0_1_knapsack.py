class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        cache = []
        for i in range(n + 1):
            row = [0] * (W + 1)
            cache.append(row)
        
        def recursiveApproach(index, limitAvailable):
            if index == n or  limitAvailable == 0:
                return 0
                
            includeIt = 0 
            if wt[index] <= limitAvailable:
                includeIt = val[index] + recursiveApproach(index + 1, limitAvailable - wt[index])
            excludeIt = recursiveApproach(index + 1, limitAvailable)
            return max(includeIt, excludeIt)
            
        def memoizationApproach(index, limitAvailable):
            if index == n or  limitAvailable == 0:
                return 0
            elif cache[index][limitAvailable] != -1:
                return cache[index][limitAvailable]
                
            includeIt = 0 
            if wt[index] <= limitAvailable:
                includeIt = val[index] + memoizationApproach(index + 1, limitAvailable - wt[index])
            excludeIt = memoizationApproach(index + 1, limitAvailable)
            
            cache[index][limitAvailable] = max(includeIt, excludeIt) 
            return cache[index][limitAvailable]
        
        def tabulationApproach():
            for index in range(n - 1, -1, -1):
                for limitAvailable in range(W, -1, -1):
                    includeIt = 0 
                    if wt[index] <= limitAvailable:
                        includeIt = val[index] + cache[index + 1][limitAvailable - wt[index]]
                    excludeIt = cache[index + 1][limitAvailable]
                    
                    cache[index][limitAvailable] = max(includeIt, excludeIt) 
            
            return cache[0][W]  
                
        
        return tabulationApproach()
