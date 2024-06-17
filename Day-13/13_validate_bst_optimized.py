# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        previous = [None]

        def findInorder(root):
            if not root:
                return True

            checkLeft = findInorder(root.left)
            if not checkLeft:
                return False
            
            if previous[0] and previous[0].val >= root.val:
                return False
            previous[0] = root

            checkRight = findInorder(root.right)
            if not checkRight:
                return False
            return True

        return findInorder(root)
        

        