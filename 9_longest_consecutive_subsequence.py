class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        result = 0

        store = set(nums)
        for ele in nums:
            if ele - 1 in store:
                continue

            currEle = ele
            currLength = 0

            while currEle in store:
                currEle += 1
                currLength += 1
            result = max(result, currLength)
        return result
