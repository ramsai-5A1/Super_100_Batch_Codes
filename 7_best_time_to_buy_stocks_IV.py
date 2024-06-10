class Solution(object):
    def maxProfit(self, K, prices):
        n = len(prices)
        def recursiveApproach(day, k, brought):
            if day == n or k == 0:
                return 0 

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + recursiveApproach(day + 1, k, 1)
                dontBuyNow = recursiveApproach(day + 1, k, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + recursiveApproach(day + 1, k - 1, 0)
                dontSellNow = recursiveApproach(day + 1, k, 1)
                maxProfit = max(sellNow, dontSellNow)

            return maxProfit

        cache = []
        for i in range(n + 1):
            row = []
            for j in range(K + 1):
                col = []
                for r in range(2):
                    col.append(0)
                row.append(col)
            cache.append(row)

        def memoizationApproach(day, k, brought):
            if day == n or k == 0:
                return 0 
            elif cache[day][k][brought] != -1:
                return cache[day][k][brought]

            maxProfit = 0
            if brought == 0:
                buyNow =  -prices[day] + memoizationApproach(day + 1, k, 1)
                dontBuyNow = memoizationApproach(day + 1, k, 0)
                maxProfit = max(buyNow, dontBuyNow)
            else:
                sellNow = prices[day] + memoizationApproach(day + 1, k - 1, 0)
                dontSellNow = memoizationApproach(day + 1, k, 1)
                maxProfit = max(sellNow, dontSellNow)
                
            cache[day][k][brought] = maxProfit 
            return maxProfit

        def tabulationApproach():
            for day in range(n - 1, -1, -1):
                for k in range(1, K + 1):
                    for brought in range(2):
                        maxProfit = 0
                        if brought == 0:
                            buyNow =  -prices[day] + cache[day + 1][k][1]
                            dontBuyNow = cache[day + 1][k][0]
                            maxProfit = max(buyNow, dontBuyNow)
                        else:
                            sellNow = prices[day] + cache[day + 1][k - 1][0]
                            dontSellNow = cache[day + 1][k][1]
                            maxProfit = max(sellNow, dontSellNow)
                        cache[day][k][brought] = maxProfit 
            return cache[0][k][0]

        return tabulationApproach()

        
