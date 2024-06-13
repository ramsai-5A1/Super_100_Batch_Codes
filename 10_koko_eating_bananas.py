class Solution(object):
    def minEatingSpeed(self, piles, h):
        n = len(piles)
        minTimeRequired = 1 
        maxTimeRequired = max(piles)

        def isPossible(val):
            hoursLeft = h 
            for ele in piles:
                if ele <= val:
                    hoursLeft -= 1 
                else:
                    hoursLeft -= (ele // val)
                    if ele % val != 0:
                        hoursLeft -= 1
                if hoursLeft < 0:
                    return False 
            return True

        left, right = minTimeRequired, maxTimeRequired
        result = -1
        while left <= right:
            mid = (left + right) // 2 
            if isPossible(mid):
                result = mid 
                right = mid - 1 
            else:
                left = mid + 1 
        return result
