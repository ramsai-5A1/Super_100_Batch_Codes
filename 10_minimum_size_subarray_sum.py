class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        left, right = 0, 0 
        result = n + 1
        currSum = 0 
        while right < n:
            currSum += nums[right]
            while currSum >= target:
                result = min(result, right - left + 1)
                currSum -= nums[left]
                left += 1
            right += 1


        return 0 if result == n + 1 else result
