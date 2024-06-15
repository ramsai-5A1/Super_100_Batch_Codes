# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        result = []
        if root == None:
            return result

        Q = []
        Q.append(root)

        while Q:
            n = len(Q)
            for i in range(n):
                current = Q.pop(0)
                if i == n - 1:
                    result.append(current.val)

                if current.left != None:
                    Q.append(current.left)

                if current.right != None:
                    Q.append(current.right)

        return result
