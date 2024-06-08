

def find_first_occurrence(nums, index, n, target):
    if index == n:
        return -1 
    elif nums[index] == target:
        return index 

    return find_first_occurrence(nums, index + 1, n, target)


nums = [10, 20, 40, 30, 40, 50, 60, 40]
target = 40
print(find_first_occurrence(nums, 0, len(nums), target))
