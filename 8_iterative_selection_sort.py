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
        
        lastIndex = n - 1 
        while lastIndex > 0:
            largeEleIndex = self.select(arr, lastIndex)
            if largeEleIndex != lastIndex:
                temp = arr[largeEleIndex]
                arr[largeEleIndex] = arr[lastIndex]
                arr[lastIndex] = temp 
            lastIndex -= 1 
