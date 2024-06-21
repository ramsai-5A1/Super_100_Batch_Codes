


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

nums = []
for ele in range(1, 10):
    nums.append(ele)
    
print(nums)
segTree = SegmentTree(nums)
ranges = [[0, 4], [1, 6], [2, 2], [5, 6], [0, 10]]
for range in ranges:
    print(range[0], range[1], " --> ", segTree.getQuerySum(range[0], range[1]))
    
segTree.update(3, 100)
segTree.update(0, -15)
print(segTree.getQuerySum(0, 3))
print(segTree.getQuerySum(0, 0))
print(segTree.getQuerySum(1, 1))
print(segTree.getQuerySum(2, 2))
print(segTree.getQuerySum(3, 3))
