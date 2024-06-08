class Solution(object):
    def climbStairs(self, n):
        def recursiveApproach(index):
            if index == n:
                return 1 
            elif index > n:
                return 0 

            oneStep = recursiveApproach(index + 1)
            twoStep = recursiveApproach(index + 2)
            return oneStep + twoStep 

        cache = [-1] * n
        def memoizationApproach(index):
            if index == n:
                return 1 
            elif index > n:
                return 0 
            elif cache[index] != -1:
                return cache[index]

            oneStep = memoizationApproach(index + 1)
            twoStep = memoizationApproach(index + 2)
            cache[index] = oneStep + twoStep 
            return cache[index]
 

        def tabulationApproach():
            cache = [-1] * (n + 2)
            cache[n] = 2 
            cache[n + 1] = 0 

            for index in range(n - 1, -1, -1):
                oneStep = memoizationApproach(index + 1)
                twoStep = memoizationApproach(index + 2)
                cache[index] = oneStep + twoStep 
            return cache[0]

        #return recursiveApproach(0)
        #return memoizationApproach(0)
        return tabulationApproach()
