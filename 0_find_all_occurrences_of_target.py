

def find_total_freqencey_of_target(nums, index, n, target):
    if index == n:
        return 0

    rightSideFrequency = find_total_freqencey_of_target(nums, index + 1, n, target)
    if nums[index] == target:
        return rightSideFrequency + 1 
    return rightSideFrequency


nums = [10, 20, 40, 30, 40, 50, 60, 40]
target = 40
print(find_total_freqencey_of_target(nums, 0, len(nums), target))
