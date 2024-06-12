class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [0] * n 
        left = 1 
        for index in range(n):
            result[index] = left 
            left *= nums[index]
        right = 1
        for index in range(n - 1, -1, -1):
            result[index] *= right 
            right *= nums[index]
        return result
