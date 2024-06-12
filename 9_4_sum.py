class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        index1 = 0 
        result = []
        while index1 < n:
            index2 = index1 + 1 
            while index2 < n:
                remaining = target - (nums[index1] + nums[index2])
                left, right = index2 + 1, n - 1 
                while left < right:
                    curr = nums[left] + nums[right]
                    if curr == remaining:
                        temp = [nums[index1], nums[index2], nums[left], nums[right]]
                        result.append(temp)

                        left += 1 
                        while left < n and nums[left] == nums[left - 1]:
                            left += 1 

                        right -= 1 
                        while right >= 0 and nums[right] == nums[right + 1]:
                            right -= 1 
                    elif curr > remaining:
                        right -= 1 
                    else:
                        left += 1 
                index2 += 1 
                while index2 < n and nums[index2] == nums[index2 - 1]:
                    index2 += 1 
                
            index1 += 1 
            while index1 < n and nums[index1] == nums[index1 - 1]:
                index1 += 1   
        return result 
