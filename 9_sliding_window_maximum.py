class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        result = []
        store = []
        
        #[300, 20, 80, 90, 150]
        # k = 4
        # [0, 1, 2, ]
        
        for i in range(k):
            # step-2 (eliminate all smaller elements indices)
            while store and nums[store[-1]] <= nums[i]:
                store.pop()
    
            # step-3 (insert current index)
            store.append(i)
        
        result.append(nums[store[0]])
        
        
        left, right = 0, k
        while right < n:
            # step-1 (eliminate unwanted indices)
            if store and store[0] == left:
                store.pop(0)

            # step-2 (eliminate all smaller elements indices)
            while store and nums[store[-1]] <= nums[right]:
                store.pop()

            # step-3 (insert current index)
            store.append(right)
            result.append(nums[store[0]])
            left += 1 
            right += 1 
            
        return result
