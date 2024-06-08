def solveIt(index, nums, n):
    if index == n:
        return 0
    nextElementsSum = solveIt(index + 1, nums, n)
    return nums[index] + nextElementsSum

nums = [1, 2, 3, 4, 11, 22]
result = solveIt(0, nums, len(nums))
print(result)
