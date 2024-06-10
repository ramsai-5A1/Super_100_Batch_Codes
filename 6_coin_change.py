class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        infValue = 1000000000

        def recursiveApproach(index, amountLeft):
            if amountLeft == 0:
                return 0
            elif index == n:
                return infValue 

            include = infValue 
            if amountLeft >= coins[index]:
                include = recursiveApproach(index, amountLeft - coins[index]) 
                if include != infValue:
                    include += 1

            exclude = recursiveApproach(index + 1, amountLeft)
            result = min(include, exclude)
            return result

        cache = [[-1] * (amount + 1) for i in range(n)]

        def memoizationApproach(index, amountLeft):
            if amountLeft == 0:
                return 0
            elif index == n:
                return infValue 
            elif cache[index][amountLeft] != -1:
                return cache[index][amountLeft]

            include = infValue 
            if amountLeft >= coins[index]:
                include = memoizationApproach(index, amountLeft - coins[index]) 
                if include != infValue:
                    include += 1

            exclude = memoizationApproach(index + 1, amountLeft)
            cache[index][amountLeft] = min(include, exclude)
            return cache[index][amountLeft]  

        def tabulationApproach():
            cache = [[infValue] * (amount + 1) for i in range(n + 1)]
            for row in range(n + 1):
                cache[row][0] = 0

            for index in range(n - 1, -1, -1):
                for amountLeft in range(amount + 1):
                    include = infValue 
                    if amountLeft >= coins[index]:
                        include = cache[index][amountLeft - coins[index]]
                        if include != infValue:
                            include += 1

                    exclude = cache[index + 1][amountLeft]
                    cache[index][amountLeft] = min(include, exclude)
            return cache[0][amount]

        result = tabulationApproach()
        if result == infValue:
            return -1 
        return result
