class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        lastIndex = n - 1 
        while lastIndex > 0:
            for index in range(lastIndex):
                if arr[index] > arr[index + 1]:
                    temp = arr[index]
                    arr[index] = arr[index + 1]
                    arr[index + 1] = temp 
            lastIndex -= 1
