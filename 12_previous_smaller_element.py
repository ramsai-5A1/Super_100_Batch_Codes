
def findPreviousSmallerElement(nums):
	n = len(nums)
	# If there is no previous smaller element, then we are considering big number as default number
	result = [10000000] * n 
	stack = []
	for index in range(n):
		while stack and stack[-1] >= nums[index]:
			stack.pop()
			
		if stack:
			result[index] = stack[-1]
		stack.append(nums[index])
	
	return result



nums = [10, -4, 5, 50, -111, 22, 3, 72, 1]
result = findPreviousSmallerElement(nums)
print(result)
