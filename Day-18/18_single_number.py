class Solution(object):
    def singleNumber(self, nums):
        mask = 0  
        for ele in nums:
            mask ^= ele 
        return mask