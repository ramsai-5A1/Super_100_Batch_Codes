class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)

        # If we don't have sufficient flowers, then return -1
        if m * k > n:
            return -1 

        def isPossible(value):
            bouquetsMade = 0
            flowersAdded = 0
            for day in range(n):
                if bloomDay[day] > value:
                    flowersAdded = 0 
                    continue
                flowersAdded += 1
                if flowersAdded == k:
                    bouquetsMade += 1 
                    if bouquetsMade == m:
                        return True
                    flowersAdded = 0
            return False

        
        minimunDays = min(bloomDay)
        maximumDays = max(bloomDay)

        left, right = minimunDays, maximumDays 
        result = -1 
        while left <= right:
            mid = (left + right) // 2 
            if isPossible(mid):
                result = mid 
                # since we need to minimize the result, so moving towards left side 
                right = mid - 1 
            else:
                left = mid + 1
        return result
