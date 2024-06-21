

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums
        self.arr = [0] * (4 * self.n)
        self.preProcess(0, self.n - 1, 0)
        
        
    def preProcess(self, left, right, index):
        if left > right:
            return 
        elif left == right:
            self.arr[index] = self.nums[left]
            return 
        
        mid = (left + right) // 2 
        leftChild = 2 * index + 1 
        rightChild = 2 * index + 2
        self.preProcess(left, mid, leftChild)
        self.preProcess(mid + 1, right, rightChild)
        self.arr[index] = self.arr[leftChild] + self.arr[rightChild]
        
        
    
    def update(self, position, ele):
        def updateHelper(left, right, index):
            # Case-1 (Complete Non Overlap)
            # Case-2 (Complete Overlap)
            # Case-3 (Partial Overlap)
            
            
            if left > right:
                return
            elif right < position or position < left:
                return
            elif position <= left and right <= position:
                self.nums[position] = ele 
                self.arr[index] = ele
                return 
                
            mid = (left + right) // 2 
            leftChild = 2 * index + 1 
            rightChild = 2 * index + 2
            
            updateHelper(left, mid, leftChild)
            updateHelper(mid + 1, right, rightChild)
            self.arr[index] = self.arr[leftChild] + self.arr[rightChild]
        
        return updateHelper(0, self.n - 1, 0)  
    
    def getQuerySum(self, l, r):
        
        def queryHelper(left, right, index):
            # Case-1 (Complete Non Overlap)
            # Case-2 (Complete Overlap)
            # Case-3 (Partial Overlap)
            
            
            if left > right:
                return 0 
            elif right < l or r < left:
                return 0 
            elif l <= left and right <= r:
                return self.arr[index]
                
            mid = (left + right) // 2 
            leftChild = 2 * index + 1 
            rightChild = 2 * index + 2
            
            leftResult = queryHelper(left, mid, leftChild)
            rightResult = queryHelper(mid + 1, right, rightChild)
            return leftResult + rightResult
        
        return queryHelper(0, self.n - 1, 0)       

class NumArray(object):

    def __init__(self, nums):
        self.segTree = SegmentTree(nums)

        

    def update(self, index, val):
        self.segTree.update(index, val)
        

    def sumRange(self, left, right):
        return self.segTree.getQuerySum(left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)