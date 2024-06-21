class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        prefixSum = [0] * n 
        for index in range(n):
            prefixSum[index] = cardPoints[index]
            if index > 0:
                prefixSum[index] += prefixSum[index - 1]
        
        result = prefixSum[k - 1]
        rightSum = 0
        lastAdded = 0
        lastIndex = n - 1
        while lastAdded < k:
            rightSum += cardPoints[lastIndex]
            leftSum = 0
            lastAdded += 1
            if k - lastAdded - 1 >= 0:
                leftSum = prefixSum[k - lastAdded - 1]
            result = max(result, leftSum + rightSum)
            lastIndex -= 1

        return result