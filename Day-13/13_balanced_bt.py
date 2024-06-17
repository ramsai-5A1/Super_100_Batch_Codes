# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        result = [True]

        def helper(currNode):
            if not currNode:
                return 0 

            leftHeight = helper(currNode.left)
            rightHeight = helper(currNode.right)
            if abs(leftHeight - rightHeight) > 1:
                result[0] = False
            return max(leftHeight, rightHeight) + 1

        helper(root)
        return result[0]