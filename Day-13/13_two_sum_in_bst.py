# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        visited = set()

        def helper(currNode):
            if not currNode:
                return False 

            otherEle = k - currNode.val 
            if otherEle in visited:
                return True 
            visited.add(currNode.val)
            leftSubtree = helper(currNode.left)
            rightSubtree = helper(currNode.right)
            return leftSubtree or rightSubtree
        return helper(root)