# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        inorder = []

        def findInorder(root):
            if not root:
                return 

            findInorder(root.left)
            inorder.append(root.val)
            findInorder(root.right)

        findInorder(root)
        for index in range(1, len(inorder)):
            if inorder[index] <= inorder[index - 1]:
                return False 
        return True

        