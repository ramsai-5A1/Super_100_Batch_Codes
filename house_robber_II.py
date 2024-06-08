class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        def robHousesUsingTabulation(startIndex, n):
            cache = [-1] * (n + 2)
            cache[n] = 0 
            cache[n + 1] = 0 
            for index in range(n - 1, startIndex - 1, -1):
                robCurrentHouse = nums[index] +  cache[index + 2]
                skipCurrentHouse = cache[index + 1]
                cache[index] = max(robCurrentHouse, skipCurrentHouse) 
            #print(startIndex, n, cache)
            return cache[startIndex]
 
 
        includeFirstEle = robHousesUsingTabulation(0, len(nums) - 1)
        excludeFirstEle = robHousesUsingTabulation(1, len(nums))
        return max(includeFirstEle, excludeFirstEle)

        
