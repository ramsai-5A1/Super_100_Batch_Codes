class Solution(object):
    def invertTree(self, root):
        if not root or (not root.left and not root.right):
            return root 

        leftChild = root.left 
        rightChild = root.right 
        root.left = self.invertTree(rightChild)
        root.right = self.invertTree(leftChild)
        return root