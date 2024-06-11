class Solution(object):
    def search(self, nums, target):

        def recursiveBinarySearch(left, right):
            if left > right:
                return -1 
            
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                return recursiveBinarySearch(left, mid - 1)
            return recursiveBinarySearch(mid + 1, right)

        return recursiveBinarySearch(0, len(nums) - 1)
