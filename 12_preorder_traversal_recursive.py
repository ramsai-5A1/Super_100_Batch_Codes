
class Solution(object):
    def preorderHelper(self, root, result):
        if root == None:
            return 
        result.append(root.val)
        self.preorderHelper(root.left, result)
        self.preorderHelper(root.right, result)

    def preorderTraversal(self, root):
        result = []
        self.preorderHelper(root, result)
        return result
