# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        store = [k]
        result = [-1]

        def collectInorderTraversal(currNode):
            if not currNode:
                return 

            collectInorderTraversal(currNode.left)
            store[0] -= 1 
            if store[0] == 0:
                result[0] = currNode.val
            collectInorderTraversal(currNode.right)

        collectInorderTraversal(root)
        return result[0]


        