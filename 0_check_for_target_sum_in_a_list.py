

def isSubsetSumPresent(nums, index, n, target):
    if target == 0:
        return True
    if index == n:
        return False 

    # At each index, we are checking for 2 possibilities.
    includeCurrentElement = False 
    if nums[index] <= target:
        includeCurrentElement = isSubsetSumPresent(nums, index + 1, n, target - nums[index])
    excludeCurrentElement = isSubsetSumPresent(nums, index + 1, n, target)

    if includeCurrentElement or excludeCurrentElement:
        return True 
    return False


nums = [10, 20, 40, 30, 40, 50, 60, 40]
target = 60
result = isSubsetSumPresent(nums, 0, len(nums), target)
if result:
    print("Sub-set target sum is found")
else:
    print("Sub-set target sum is not found")
