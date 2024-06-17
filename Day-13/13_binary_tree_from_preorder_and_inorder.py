# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        store = dict()
        n = len(inorder)
        for index in range(n):
            store[inorder[index]] = index

        index = [0]
        def helper(left, right):
            if left > right:
                return None 

            node = TreeNode(preorder[index[0]])
            index[0] += 1 
            node.left = helper(left, store[node.val] - 1)
            node.right = helper(store[node.val] + 1, right)
            return node



        return helper(0, n - 1)

        