class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = []
        nums.sort()

        index = 0
        while index < n:
            subTarget = 0 - nums[index]
            left, right = index + 1, n - 1
            while left < right:
                currSum = nums[left] + nums[right]
                if currSum == subTarget:
                    subTriplet = [nums[index], nums[left], nums[right]]
                    result.append(subTriplet)
                    left += 1
                    while left < n and  nums[left] == nums[left - 1]:
                        left += 1

                    right -= 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1

                elif currSum > subTarget:
                    right -= 1
                else:
                    left += 1
            index += 1
            while index < n and nums[index] == nums[index - 1]:
                index += 1
        return result
        
