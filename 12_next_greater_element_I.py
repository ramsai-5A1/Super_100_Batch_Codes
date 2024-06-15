class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n2 = len(nums2)
        stack = []
        result = [-1] * n2
        store = dict()
        for index in range(n2 - 1, -1, -1):
            store[nums2[index]] = index
            while stack and nums2[stack[-1]] <= nums2[index]:
                stack.pop()
            if stack:
                result[index] = stack[-1]
            stack.append(index)

        n1 = len(nums1)
        finalResult = [-1] * n1
        for index in range(n1):
            finalResult[index] = result[store[nums1[index]]]
            if finalResult[index] != -1:
                finalResult[index] = nums2[finalResult[index]]
        return finalResult
