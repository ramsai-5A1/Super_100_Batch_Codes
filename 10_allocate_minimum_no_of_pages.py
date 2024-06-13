class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        if M > N:
            return -1
        
        left, right = min(A), sum(A)
        result = -1 
        
        def isPossible(mid):
            currStudents = 1 
            currSum = 0 
            for ele in A:
                if ele > mid:
                    return False 
                elif ele + currSum <= mid:
                    currSum += ele 
                else:
                    currSum = ele 
                    currStudents += 1 
                    
            return currStudents <= M 
        #print(N, M)
        #print(A)
        while left <= right:
            mid = (left + right) // 2 
            #print(mid, isPossible(mid))
            if isPossible(mid):
                result = mid 
                right = mid - 1 
            else:
                left = mid + 1
        
        return result
        

