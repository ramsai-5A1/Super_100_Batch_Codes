class Solution(object):
    def subsets(self, nums):
        result = []
        n = len(nums)
        N = 1 << n
        for i in range(N):
            curr = []
            # 101
            for j in range(31):
                if i & (1 << j):
                    curr.append(nums[j])
            result.append(curr)
        return result
        