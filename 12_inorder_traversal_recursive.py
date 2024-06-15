class Solution(object):
    def inorderHelper(self, root, result):
        if root == None:
            return 
        
        self.inorderHelper(root.left, result)
        result.append(root.val)
        self.inorderHelper(root.right, result)

    def inorderTraversal(self, root):
        result = []
        self.inorderHelper(root, result)
        return result
