class Solution:
    def merge(self,nums, left, mid, right): 
        # code here
        temp = []
        index1 = left 
        index2 = mid + 1 
     
        while index1 <= mid and index2 <= right:
            if nums[index1] < nums[index2]:
                temp.append(nums[index1])
                index1 += 1 
            else:
                temp.append(nums[index2])
                index2 += 1 
     
        while index1 <= mid:
            temp.append(nums[index1])
            index1 += 1 
     
        while index2 <= right:
            temp.append(nums[index2])
            index2 += 1 
     
     
        index = left 
        for ele in temp:
            nums[index] = ele 
            index += 1
        
    def mergeSort(self,nums, left, right):
        #code here
        if left >= right:
            return
 
        mid = (left + right) // 2 
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
