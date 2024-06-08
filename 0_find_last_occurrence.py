

def find_last_occurrence(nums, n, target):
    if n == 0:
        return -1 
    elif nums[n - 1] == target:
        return n - 1 

    return find_last_occurrence(nums, n - 1, target)


nums = [10, 20, 40, 30, 40, 50, 60, 40]
target = 40
print(find_last_occurrence(nums, len(nums), target))
