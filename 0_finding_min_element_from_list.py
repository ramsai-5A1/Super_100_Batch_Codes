def solveIt(index, nums, n):
    if index == n:
        return 1000000000
    minEleInRightPart = solveIt(index + 1, nums, n)
    if nums[index] < minEleInRightPart:
        return nums[index]
    return minEleInRightPart

nums = [1, 2, 3, 4, 11, 22]
result = solveIt(0, nums, len(nums))
print(result)
