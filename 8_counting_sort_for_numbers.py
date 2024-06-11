


def performCountingSort(nums, n):
    # step-1: finding max element 
    mx = max(nums)
    
    # step-2: initializing (mx + 1) sized array with all zeroes
    store = [0] * (mx + 1)
    
    # step-3: finding frequency of each element
    for ele in nums:
        store[ele] += 1 
        
    # step-4: calculating prefix sum
    for index in range(1, mx + 1):
        store[index] += store[index - 1] 
        
    # step-5: place each element at its corresponding element
    temp = [-1] * n
    for index in range(n - 1, -1, -1):
        value = nums[index]
        store[value] -= 1 
        temp[store[value]] = value 
        
    # step-6: copy from temporary list to actual list 
    for index in range(n):
        nums[index] = temp[index]


nums = [6, 5, 5, 5, 3, 1, 5, 1, 2, 4]
print("Before sorting:", nums)
performCountingSort(nums, len(nums))
print("After sorting:", nums)
