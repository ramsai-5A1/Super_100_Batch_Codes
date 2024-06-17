# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        minStack = [[root, 1]]
        maxStack = [[root, 1]]

        def getNextLeftValue():
            while minStack:
                curr = minStack[-1]
                if curr[1] == 1:
                    curr[1] += 1 
                    if curr[0].left:
                        minStack.append([curr[0].left, 1]) 
                elif curr[1] == 2:
                    curr[1] += 1 
                    if curr[0].right:
                        minStack.append([curr[0].right, 1])
                    return curr[0].val
                else:
                    minStack.pop()
            return 10000000

        def getPrevRightValue():
            while maxStack:
                curr = maxStack[-1]
                if curr[1] == 1:
                    curr[1] += 1 
                    if curr[0].right:
                        maxStack.append([curr[0].right, 1]) 
                elif curr[1] == 2:
                    curr[1] += 1 
                    if curr[0].left:
                        maxStack.append([curr[0].left, 1])
                    return curr[0].val
                else:
                    maxStack.pop()
            return -10000000
        

        left = getNextLeftValue() 
        right = getPrevRightValue() 
        while left < right:
            currSum = left + right 
            if currSum == k:
                return True 
            elif currSum > k:
                right = getPrevRightValue() 
            else:
                left = getNextLeftValue()
        return False