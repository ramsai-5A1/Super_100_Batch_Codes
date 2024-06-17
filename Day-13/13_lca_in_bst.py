# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None 

        currNode = root 
        while currNode:
            if currNode.val > p.val and currNode.val > q.val:
                currNode = currNode.left 
            elif currNode.val < p.val and currNode.val < q.val:
                currNode = currNode.right 
            else:
                return currNode 
        return None