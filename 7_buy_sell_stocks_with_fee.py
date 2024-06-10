class Solution(object):
    def maxProfit(self, prices, fee):
        n = len(prices)
        def recursiveApproach(day, brought):
            if day == n:
                return 0 

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + recursiveApproach(day + 1, 1)
                dontBuyNow = recursiveApproach(day + 1, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + recursiveApproach(day + 1, 0) - fee
                dontSellNow = recursiveApproach(day + 1, 1)
                maxProfit = max(sellNow, dontSellNow)

            return maxProfit

        cache = []
        for i in range(n + 1):
            row = []
            for j in range(2):
                row.append(0)
            cache.append(row)

        def memoizationApproach(day, brought):
            if day == n:
                return 0 
            elif cache[day][brought] != -1:
                return cache[day][brought]

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + memoizationApproach(day + 1, 1)
                dontBuyNow = memoizationApproach(day + 1, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + memoizationApproach(day + 1, 0) - fee
                dontSellNow = memoizationApproach(day + 1, 1)
                maxProfit = max(sellNow, dontSellNow)
                
            cache[day][brought] = maxProfit 
            return maxProfit

        def tabulationApproach():
            for day in range(n - 1, -1, -1):
                for brought in range(2):
                    maxProfit = 0
                    if brought == 0:
                        buyNow =  -prices[day] + cache[day + 1][1]
                        dontBuyNow = cache[day + 1][0]
                        maxProfit = max(buyNow, dontBuyNow)
                    else:
                        sellNow = prices[day] + cache[day + 1][0] - fee
                        dontSellNow = cache[day + 1][1]
                        maxProfit = max(sellNow, dontSellNow)
                    cache[day][brought] = maxProfit 
            return cache[0][0]

        return tabulationApproach()
        
