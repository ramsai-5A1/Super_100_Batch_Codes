def solveIt(index, nums, n):
    if index == n:
        return 0
    maxEleInRightPart = solveIt(index + 1, nums, n)
    if nums[index] > maxEleInRightPart:
        return nums[index]
    return maxEleInRightPart

nums = [1, 2, 3, 4, 11, 22]
result = solveIt(0, nums, len(nums))
print(result)
