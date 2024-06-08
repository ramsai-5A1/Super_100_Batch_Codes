#User function Template for python3

class Solution:
        
    def add(self, a, b):
        mod = 1000000007
        a %= mod 
        b %= mod 
        return (a + b) % mod
    
    def topDown(self, n):
        cache = [-1] * (n + 1)
        
        
        def topDownHelper(n):
            mod = 1000000007
            
            if n == 0:
                return 0 
            elif n == 1:
                return 1 
            elif n == 2:
                return 2
            elif cache[n] != -1:
                return cache[n]
                
            cache[n] = self.add(topDownHelper(n - 1), topDownHelper(n - 2))
            return cache[n]
        return topDownHelper(n)
        
    def bottomUp(self, n):
        mod = 1000000007
        cache = [-1] * (n + 1)
        cache[0] = 0 
        cache[1] = 1 
        
        for index in range(2, n + 1):
            cache[index] = self.add(cache[index - 1], cache[index - 2]) 
        return cache[n]
        
        
        
        
