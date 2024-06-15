def findPreviousGreaterElement(nums):
	n = len(nums)
	result = [-1] * n 
	stack = []
	for index in range(n):
		while stack and stack[-1] <= nums[index]:
			stack.pop()
			
		if stack:
			result[index] = stack[-1]
		stack.append(nums[index])
	
	return result



nums = [10, -4, 5, 50, -111, 22, 3, 72, 1]
result = findPreviousGreaterElement(nums)
print(result)
