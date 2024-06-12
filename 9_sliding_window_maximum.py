class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        dq = []
        n = len(nums)
        for index in range(n):

            while len(dq) > 0 and dq[0][0] <= index - k:
                dq.pop(0)

            while len(dq) > 0 and dq[-1][1] <= nums[index]:
                dq.pop()

            dq.append([index, nums[index]])
            if index >= k - 1:
                result.append(dq[0][1])

        return result
