class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        box = {}
        for index in range(n - 1, -1, -1):
            otherElement = target - nums[index]
            if otherElement in box:
                return [index, box[otherElement]]

            box[nums[index]] = index

        return []            
