class Solution:
    def insert(self, alist, index, n):
        currEle = alist[index]
        prevIndex = index - 1 
        while prevIndex >= 0:
            if alist[prevIndex] > currEle:
                alist[prevIndex + 1] = alist[prevIndex]
            else:
                break 
            prevIndex -= 1 
        alist[prevIndex + 1] = currEle
        
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        if n == 1:
            return 
        
        self.insertionSort(alist, n - 1)
        self.insert(alist, n - 1, n)
