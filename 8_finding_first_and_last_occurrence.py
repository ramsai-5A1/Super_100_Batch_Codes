class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        result = [-1, -1]

        def findFirstOccurrence():
            left, right = 0, n - 1 
            position = -1
            while left <= right:
                mid = (left + right) // 2 
                if nums[mid] == target:
                    position = mid 
                    right = mid - 1 
                elif nums[mid] > target:
                    right = mid - 1 
                else:
                    left = mid + 1 
            return position 

        def findLastOccurrence():
            left, right = 0, n - 1 
            position = -1
            while left <= right:
                mid = (left + right) // 2 
                if nums[mid] == target:
                    position = mid 
                    left = mid + 1 
                elif nums[mid] > target:
                    right = mid - 1 
                else:
                    left = mid + 1 
            return position  

        result[0] = findFirstOccurrence() 
        result[1] = findLastOccurrence()
        return result
