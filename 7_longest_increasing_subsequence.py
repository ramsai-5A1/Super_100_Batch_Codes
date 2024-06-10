class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)

        def recursiveApproach(index, prevIndex):
            if index == n:
                return 0 

            include = 0
            if prevIndex == -1 or nums[prevIndex] < nums[index]:
                include = 1 + recursiveApproach(index + 1, index) 
            exclude = recursiveApproach(index + 1, prevIndex)
            return max(include, exclude)

        # index can range from 0 till n - 1 
        # prevIndex can range from -1 till n - 1 
        cache = [[-1] * (n) for i in range(n + 1)]

        def memoizationApproach(index, prevIndex):
            if index == n:
                return 0 
            elif cache[prevIndex + 1][index] != -1:
                return cache[prevIndex + 1][index]

            include = 0
            if prevIndex == -1 or nums[prevIndex] < nums[index]:
                include = 1 + memoizationApproach(index + 1, index) 
            exclude = memoizationApproach(index + 1, prevIndex)
            cache[prevIndex + 1][index] = max(include, exclude)
            return cache[prevIndex + 1][index]

        def tabulationApproach():
            result = [1] * n 
            finalLis = 1
            for index in range(1, n): 
                for prevIndex in range(index):
                    if nums[index] > nums[prevIndex]:
                        result[index] = max(result[index], result[prevIndex] + 1)
                finalLis = max(finalLis, result[index])
            return finalLis

        return tabulationApproach()
       
        
