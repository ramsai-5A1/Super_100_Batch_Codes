# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        inorder = []

        def collectInorderTraversal(currNode):
            if not currNode:
                return 

            collectInorderTraversal(currNode.left)
            inorder.append(currNode.val)
            collectInorderTraversal(currNode.right)

        collectInorderTraversal(root)
        return inorder[k - 1]


        