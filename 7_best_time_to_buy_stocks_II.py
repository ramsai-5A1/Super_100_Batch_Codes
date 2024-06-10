class Solution(object):
    def maxProfit(self, prices):
        result = 0 
        n = len(prices)
        for index in range(1, n):
            if prices[index] > prices[index - 1]:
                result += (prices[index] - prices[index - 1])
        return result
        
