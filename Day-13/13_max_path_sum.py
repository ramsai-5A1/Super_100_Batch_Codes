# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        result = [-1000000000]

        def helper(currNode):
            if currNode == None:
                return 0 
            elif currNode.left == None and currNode.right == None:
                result[0] = max(result[0], currNode.val)
                return max(0, currNode.val)

            
            leftMaxValue = helper(currNode.left)
            rightMaxValue = helper(currNode.right)
            # logic here
            value1 = currNode.val
            value2 = currNode.val + leftMaxValue
            value3 = currNode.val + rightMaxValue
            value4 = leftMaxValue + currNode.val + rightMaxValue
            result[0] = max([result[0], value1, value2, value3, value4])
            
            return currNode.val + max([leftMaxValue, rightMaxValue])
             

        helper(root)
        return result[0]