class Solution:
    #Function to sort a list using quick sort algorithm.
    def partition(self,nums,left,right):
        # code here
        pivot = nums[right]
        position = left 
     
        for index in range(left, right):
            if nums[index] <= pivot:
                temp = nums[index]
                nums[index] = nums[position]
                nums[position] = temp
                position += 1 
     
        # 12, 13, 10, 22, 20, 18, 16
        # 12, 13, 10, 16, 20, 18, 22
        nums[position], nums[right] = nums[right], nums[position]
        return position
    
    def quickSort(self,nums,left,right):
        # code here
        if left >= right:
            return
 
        pivotIndex = self.partition(nums, left, right)
        self.quickSort(nums, left, pivotIndex - 1)
        self.quickSort(nums, pivotIndex + 1, right)
