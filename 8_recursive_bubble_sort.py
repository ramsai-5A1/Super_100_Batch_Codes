class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        if n == 1:
            return 
        for index in range(n - 1):
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1] = temp 
        self.bubbleSort(arr, n - 1)
