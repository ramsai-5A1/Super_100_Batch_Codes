class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        for index in range(1, n):
            nums[index] += nums[index - 1]
        self.nums = nums
        

    def sumRange(self, left, right):
        result = self.nums[right]
        return result if left == 0 else result - self.nums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)