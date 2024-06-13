class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        result = 0 
        zeroesFlippedToOnes = 0 
        onesCount = 0
        left, right = 0, 0

        while right < n:
            if nums[right] == 1:
                onesCount += 1 
            elif zeroesFlippedToOnes < k:
                # If we can convert a zero to one, then we are converting it here
                zeroesFlippedToOnes += 1 
            else:
                while zeroesFlippedToOnes == k:
                    if nums[left] == 0:
                        # If we've flipped earlier 0 to 1, then we are removing that count
                        zeroesFlippedToOnes -= 1
                    left += 1
                # Now counting the current 0
                zeroesFlippedToOnes += 1
            result = max(result, right - left + 1)
            right += 1
        return result
