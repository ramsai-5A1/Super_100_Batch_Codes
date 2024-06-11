class Solution: 
    def select(self, arr, i):
        largeEleIndex = i 
        for index in range(i):
            if arr[index] > arr[largeEleIndex]:
                largeEleIndex = index 
        return largeEleIndex
    
    def selectionSort(self, arr,n):
        if n == 1:
            return 
        
        
        largeEleIndex = self.select(arr, n - 1)
        if largeEleIndex != n - 1:
            temp = arr[largeEleIndex]
            arr[largeEleIndex] = arr[n - 1]
            arr[n - 1] = temp 
        
        self.selectionSort(arr, n - 1)
