
def checKIsOdd(n):
    if n & 1 == 1:
        return True 
    return False

def swapTwoNumbers(a, b):
    print("Before swapping, a:", a, "b:", b)
    a = a ^ b 
    b = a ^ b 
    a = a ^ b 
    print("After swapping, a:", a, "b:", b)

def checkIthBitIsSet(n, i):
    if (n & (1 << i)):
        return True 
    return False

def setIthBit(n, i):
    print("Before setting", i, "th bit", n)
    n = n | (1 << i)
    print("After setting", i, "th bit", n)

def clearIthBit(n, i):
    print("Before clearing", i, "th bit", n)
    n = n & (~(1 << i))
    print("After clearing", i, "th bit", n)

def toggleIthBit(n, i):
    print("Before toggling", i, "th bit", n)
    n = n ^ (1 << i)
    print("After toggling", i, "th bit", n) 

def removeLastSetBit(n):
    print("Before removing last bit", n)
    n = n & (n - 1)
    print("After removing last bit", n) 

def checKIfNumberIsPowerOfTwo(n):
    if n & (n - 1) == 0:
        return True 
    return False
    

def countNumberOfSetBits(n):
    result = 0 
    # while n > 0:
    #     if n & 1:
    #         result += 1 
    #     n >>= 1 
    
    while n > 0:
        n = n & (n - 1)
        result += 1
    
    return result

def powerSet(nums):
    n = len(nums)
    N = (1 << n)
    result = []
    print(N)
    
    for curr in range(N):
        temp = []
        for i in range(n + 1):
            if (curr & (1 << i)):
                temp.append(nums[i])
        result.append(temp)
    
    return result

def divideByTwo(n):
    return n >> 1 
    

def calculateTwoPowerN(n):
    return 1 << n 
    
def multiplyWithTwo(n):
    return n << 1 
    
    
    
print(divideByTwo(10))
print(divideByTwo(13))

print(calculateTwoPowerN(3))
print(calculateTwoPowerN(5))

print(multiplyWithTwo(3))
print(multiplyWithTwo(6))

# print(checKIsOdd(1))
# print(checKIsOdd(5))
# print(checKIsOdd(10))



# a, b = 10, 20 
# swapTwoNumbers(a, b)


# print(checkIthBitIsSet(9, 0))
# print(checkIthBitIsSet(10, 1))
# print(checkIthBitIsSet(10, 2))
# print(checkIthBitIsSet(10, 3))
# print(checkIthBitIsSet(10, 4))


# setIthBit(10, 0)
# setIthBit(10, 1)
# setIthBit(10, 2)


# clearIthBit(10, 0)
# clearIthBit(10, 1)
# clearIthBit(10, 3)

# toggleIthBit(10, 0)
# toggleIthBit(10, 1)
# toggleIthBit(10, 3)


# removeLastSetBit(10)
# removeLastSetBit(8)
# removeLastSetBit(11)

# print(checKIfNumberIsPowerOfTwo(8))
# print(checKIfNumberIsPowerOfTwo(7))
# print(checKIfNumberIsPowerOfTwo(12))
# print(checKIfNumberIsPowerOfTwo(32))




# print(countNumberOfSetBits(10))
# print(countNumberOfSetBits(11))
# print(countNumberOfSetBits(7))
#print(powerSet([1, 2, 3, 4, 5]))



