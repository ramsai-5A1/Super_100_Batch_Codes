class Solution(object):
    def flatten(self, root):
        if not root or (not root.left and not root.right):
            return

        leftChild = root.left 
        rightChild = root.right
        root.left = None
        self.flatten(leftChild)
        self.flatten(rightChild)

        root.right = leftChild
        curr = root 
        while curr.right:
            curr = curr.right 
        
        curr.right = rightChild