class Solution(object):
    def maxScore(self, cardPoints, k):
        result = 0 
        currTotal = sum(cardPoints[:k])
        result = currTotal
        left, right = k - 1, len(cardPoints) - 1 
        while left >= 0:
            currTotal -= cardPoints[left]
            currTotal += cardPoints[right]
            result = max(result, currTotal)
            left -= 1 
            right -= 1 
        return result
        
