class Solution(object):
    def countPrimes(self, n):
        isPrime = [True] * (n + 1)
    
        currNumber = 2 
        while currNumber * currNumber <= n:
            if isPrime[currNumber]:
                # Marking all multiples as not prime 
                for currNumMultiple in range(2 * currNumber, n + 1, currNumber):
                    isPrime[currNumMultiple] = False 
            currNumber += 1 
        
        result = 0 
        if 2 < n:
            result += 1
        
        # Just itterating all odd numbers, as even number can't be prime
        for num in range(3, n, 2):
            if isPrime[num]:
                result += 1 
        return result