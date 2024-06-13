class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)
        rightSideGrumpy = [0] * (n + 1)
        leftSideGrumpy = [0] * (n + 1) 
        for index in range(n):
            if grumpy[index] == 0:
                leftSideGrumpy[index] = customers[index]
            if index > 0:
                leftSideGrumpy[index] += leftSideGrumpy[index - 1]

        for index in range(n - 1, -1, -1):
            if grumpy[index] == 0:
                rightSideGrumpy[index] = customers[index]
            if index < n - 1:
                rightSideGrumpy[index] += rightSideGrumpy[index + 1]

        result = 0 
        currSum = sum(customers[:minutes]) 
        result = currSum + rightSideGrumpy[minutes]
        left, right = 0, minutes

        while right < n:
            currSum -= customers[left]
            currSum += customers[right]
            currentResult = currSum + rightSideGrumpy[right + 1] + leftSideGrumpy[left]
            result = max(result, currentResult)
            left += 1 
            right += 1
        
        return result
