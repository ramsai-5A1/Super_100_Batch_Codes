class Solution:
    def sumSubarrayMins(self, N, fruits):
        result = 0 
        left, right = 0, 0 
        baskets = dict()
        
        while right < N:
            currFruit = fruits[right]
            if currFruit in baskets:
                baskets[currFruit] += 1 
            elif len(baskets) < 2:
                baskets[currFruit] = 1 
            else:
                while len(baskets) == 2:
                    leftIndexFruit = fruits[left]
                    baskets[leftIndexFruit] -= 1 
                    if baskets[leftIndexFruit] == 0:
                        baskets.pop(leftIndexFruit)
                    left += 1 
                baskets[currFruit] = 1 
            result = max(result, right - left + 1)
            right += 1
            
        return result
