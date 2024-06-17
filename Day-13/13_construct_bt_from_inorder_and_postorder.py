class Solution(object):
    def buildTree(self, inorder, postorder):
        store = dict()
        n = len(inorder)
        for index in range(n):
            store[inorder[index]] = index 
        index = [n - 1]

        def helper(left, right):
            if left > right:
                return None 

            currNode = TreeNode(postorder[index[0]])
            index[0] -= 1
            currNode.right = helper(store[currNode.val] + 1, right)
            currNode.left = helper(left, store[currNode.val] - 1)
            return currNode
            
        return helper(0, n - 1)