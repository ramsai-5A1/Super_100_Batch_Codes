
def display_left_to_right(nums, index, n):
    if index == n:
        print()
        return 

    print(nums[index], end = " ")
    display_left_to_right(nums, index + 1, n)


def display_right_to_left(nums, n):
    if n == 0:
        print()
        return

    print(nums[n - 1], end = " ")
    display_right_to_left(nums, n - 1)


nums = [10, 20, 30, 40, 50, 60]
display_left_to_right(nums, 0, len(nums))
display_right_to_left(nums, len(nums))
