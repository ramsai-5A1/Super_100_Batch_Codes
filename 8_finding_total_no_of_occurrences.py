class Solution:

	def count(self,arr, n, x):
		def findFirstOccurrence():
            left, right = 0, n - 1 
            position = -1
            while left <= right:
                mid = (left + right) // 2 
                if arr[mid] == x:
                    position = mid 
                    right = mid - 1 
                elif arr[mid] > x:
                    right = mid - 1 
                else:
                    left = mid + 1 
            return position 

        def findLastOccurrence():
            left, right = 0, n - 1 
            position = -1
            while left <= right:
                mid = (left + right) // 2 
                if arr[mid] == x:
                    position = mid 
                    left = mid + 1 
                elif arr[mid] > x:
                    right = mid - 1 
                else:
                    left = mid + 1 
            return position  

        firstIndex = findFirstOccurrence() 
        if firstIndex == -1:
            return 0
        lastIndex = findLastOccurrence()
        return lastIndex - firstIndex + 1
