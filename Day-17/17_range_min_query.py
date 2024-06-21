#User function Template for python3

def constructST(arr,n):
    stArr = [-1] * (4 * n)
    
    def constructHelper(left, right, index):
        if left > right:
            return 100000000 
        elif left == right:
            stArr[index] = arr[left]
            return arr[left]
            
        mid = (left + right) >> 1 
        leftMin = constructHelper(left, mid, 2 * index + 1)
        rightMin = constructHelper(mid + 1, right, 2 * index + 2)
        stArr[index] = min(leftMin, rightMin)
        return stArr[index]
        
    constructHelper(0, n - 1, 0)
    return stArr

def RMQ(st ,  n,  qs,  qe):
    
    def RMQHelper(left, right, index):
        if qs <= left and right <= qe:
            return st[index]
        elif right < qs or qe < left:
            return 100000000 
        
        mid = (left + right) >> 1 
        leftMin = RMQHelper(left, mid, 2 * index + 1)
        rightMin = RMQHelper(mid + 1, right, 2 * index + 2)
        return min(leftMin, rightMin)
        
    return RMQHelper(0, n - 1, 0)

