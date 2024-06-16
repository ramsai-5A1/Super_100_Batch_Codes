class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)


        def findPreviousSmaller():
            result = [-1] * n 
            stack = []

            for index in range(n):
                while stack and heights[stack[-1]] >= heights[index]:
                    stack.pop()

                if stack:
                    result[index] = stack[-1]
                stack.append(index)
            return result 

        def findNextSmaller():
            result = [n] * n 
            stack = []

            for index in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[index]:
                    stack.pop()

                if stack:
                    result[index] = stack[-1]
                stack.append(index)
            return result 

        result = 0 
        leftSmaller = findPreviousSmaller()
        rightSmaller = findNextSmaller()
        

        for index in range(n):
            height = heights[index]
            breadth = rightSmaller[index] - leftSmaller[index] - 1
            currArea = height * breadth 
            result = max(result, currArea)
        return result
