class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        mask = 0 
        for i in range(n + 1):
            mask ^= i 

        for ele in nums:
            mask ^= ele 
        return mask
        