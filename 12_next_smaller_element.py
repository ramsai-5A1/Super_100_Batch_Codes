def nextSmallerElement(arr,n):
    result = [-1] * n  
    stack = []
    for index in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[index]:
            stack.pop()

        if stack:
            result[index] = stack[-1]
        stack.append(arr[index])

    return result
