class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0] * n

        stack = []
        for index in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[index]:
                stack.pop()

            if stack:
                result[index] = stack[-1] - index

            stack.append(index)\
            
        return result
