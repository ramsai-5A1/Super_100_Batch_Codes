class Solution:
    def firstIndex(self, arr, n):
        left, right = 0, n - 1 
        result = -1 
        
        while left <= right:
            mid = (left + right) // 2 
            if arr[mid] == 1:
                result = mid 
                right = mid - 1 
            else:
                left = mid + 1
        
        return result
