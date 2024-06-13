class Solution(object):
    def shipWithinDays(self, weights, days):
        # if we get 'n' number of 'days' available, then we can transfer each package on each day
        # then to transfer the maximum weighted package, we need to have that much as our capacity
        minWeight = max(weights)

        # if we get one 'day' available, then we need to transfer all the packages at once, 
        # so we need to ship all the packages at once
        maxWeight = sum(weights)

        def isPossible(value):
            currentLoad = 0
            noOfDaysLeft = days - 1
            for package in weights:
                if package > value:
                    return False
                if currentLoad + package > value:
                    currentLoad = package 
                    noOfDaysLeft -= 1 
                    if noOfDaysLeft < 0:
                        return False
                else:
                    currentLoad += package 
            return True
                

        left, right = minWeight, maxWeight 
        result = -1
        while left <= right:
            mid = (left + right) // 2 
            if isPossible(mid):
                result = mid 
                # we need to look out for minimum possible so moving towards left
                right = mid - 1
            else:
                left = mid + 1 
        return result
