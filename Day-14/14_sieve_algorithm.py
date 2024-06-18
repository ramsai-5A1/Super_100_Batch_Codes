

# Program to calculate all primes upto N using Sieve algorithm 

def findAllPrimesUsingSieveAlgo(n):
    isPrime = [True] * (n + 1)
    
    currNumber = 2 
    while currNumber * currNumber <= n:
        if isPrime[currNumber]:
            # Marking all multiples as not prime 
            for currNumMultiple in range(2 * currNumber, n + 1, currNumber):
                isPrime[currNumMultiple] = False 
        currNumber += 1 
        
    primes = []
    primes.append(2)
    
    # Just itterating all odd numbers, as even number can't be prime
    for num in range(3, n + 1, 2):
        if isPrime[num]:
            primes.append(num)
            
    return primes


n = int(input())
result = findAllPrimesUsingSieveAlgo(n)
print(result)