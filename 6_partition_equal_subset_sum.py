lass Solution(object):
    def canPartition(self, nums):
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False 

        total = total // 2 

        def recursiveApproach(index, totalRemaining):
            if index == n:
                return False if totalRemaining != 0 else True
            elif totalRemaining == 0:
                return False 

            include = False 
            if totalRemaining >= nums[index]:
                include = recursiveApproach(index + 1, totalRemaining - nums[index])

            exclude = recursiveApproach(index + 1, totalRemaining)
            result = include or exclude 
            return result


            
        cache = [[-1] * (total + 1) for i in range(n)]
        
        def memoizationApproach(index, totalRemaining):
            if index == n:
                return False if totalRemaining != 0 else True
            elif totalRemaining == 0:
                return False 
            elif cache[index][totalRemaining] != -1:
                return True if cache[index][totalRemaining] == 1 else False 

            include = False 
            if totalRemaining >= nums[index]:
                include = memoizationApproach(index + 1, totalRemaining - nums[index])

            exclude = memoizationApproach(index + 1, totalRemaining)
            result = include or exclude 
            cache[index][totalRemaining] = 1 if result else 0
            return result

        def tabulationApproach():
            cache = [[False] * (total + 1) for i in range(n + 1)] 
            cache[n][0] = True

            for index in range(n - 1, -1, -1):
                for totalRemaining in range(total + 1):
                    include = False 
                    if totalRemaining >= nums[index]:
                        include = cache[index + 1][totalRemaining - nums[index]]

                    exclude = cache[index + 1][totalRemaining]
                    result = include or exclude 
                    cache[index][totalRemaining] = result 
            return cache[0][total]


        # return recursiveApproach(0, total)
        # return memoizationApproach(0, total)
        return tabulationApproach()
