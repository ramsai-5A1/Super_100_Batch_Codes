class Solution(object):
    def rob(self, nums):
        n = len(nums)
        cache = [-1] * n
        def robHousesUsingRecursion(index):
            if index >= n:
                return 0 

            robCurrentHouse = nums[index] +  robHousesUsingRecursion(index + 2)
            skipCurrentHouse = robHousesUsingRecursion(index + 1)
            return max(robCurrentHouse, skipCurrentHouse)

        def robHousesUsingMemoization(index):
            if index >= n:
                return 0 
            elif cache[index] != -1:
                return cache[index]

            robCurrentHouse = nums[index] +  robHousesUsingRecursion(index + 2)
            skipCurrentHouse = robHousesUsingRecursion(index + 1)
            cache[index] = max(robCurrentHouse, skipCurrentHouse) 
            return cache[index]

        def robHousesUsingTabulation():
            cache = [-1] * (n + 2)
            cache[n] = 0 
            cache[n + 1] = 0 
            for index in range(n - 1, -1, -1):
                robCurrentHouse = nums[index] +  cache[index + 2]
                skipCurrentHouse = cache[index + 1]
                cache[index] = max(robCurrentHouse, skipCurrentHouse) 
            return cache[0]


        return robHousesUsingTabulation()
        
