class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        result = right

        def isPossible(mid):
            val = k 
            curr = 0
            for ele in nums:
                if ele > mid:
                    return False
                if curr + ele > mid:
                    curr = ele 
                    val -= 1 
                    if val == 0:
                        return False 
                else:
                    curr += ele
            return True

        while left <= right:
            mid = left + ((right - left) // 2 )
            if isPossible(mid):
                result = mid 
                right = mid - 1 
            else:
                left = mid + 1 
        return result
        
