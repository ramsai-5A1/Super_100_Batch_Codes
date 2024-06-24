class Solution:
    def bitManipulation(self, num, i):
        def getIthBitIsSet(n, i):
            return 1 if (n & (1 << i)) else 0
            
        
        def setIthBit(n, i):
            return n | (1 << i)
        
        
        def clearIthBit(n, i):
            return n & (~(1 << i))
        
        result1 = getIthBitIsSet(num, i - 1)
        result2 = setIthBit(num, i - 1)
        result3 = clearIthBit(num, i - 1)
        print(result1, result2, result3)