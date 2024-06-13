class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        result = 0 
        currSum = sum(Arr[:K])
        result = currSum
        left, right = 0, K 
        while right < N:
            currSum -= Arr[left]
            currSum += Arr[right]
            result = max(result, currSum)
            left += 1 
            right += 1
        return result
