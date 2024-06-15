class Solution(object):
    def postorderHelper(self, root, result):
        if root == None:
            return 
        
        self.postorderHelper(root.left, result)
        self.postorderHelper(root.right, result)
        result.append(root.val)

    def postorderTraversal(self, root):
        result = []
        self.postorderHelper(root, result)
        return result
