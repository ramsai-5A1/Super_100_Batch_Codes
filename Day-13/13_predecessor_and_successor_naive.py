class Solution:
    def findPreSuc(self, root, pre, suc, key):
        inorder = []
        def collectInorder(currNode):
            if not currNode:
                return 
            
            collectInorder(currNode.left)
            inorder.append(currNode.key)
            collectInorder(currNode.right)
        collectInorder(root)
        
        
        n = len(inorder)
        for index in range(n):
            if inorder[index] < key:
                pre.key = inorder[index]
            if inorder[index] > key:
                suc.key = inorder[index]
                break