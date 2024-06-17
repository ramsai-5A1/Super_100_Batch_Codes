#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        inorder = []

        def collectInorderTraversal(currNode):
            if not currNode:
                return 

            collectInorderTraversal(currNode.left)
            inorder.append(currNode.data)
            collectInorderTraversal(currNode.right)

        collectInorderTraversal(root)
        inorder = inorder[::-1]
        return inorder[k - 1]
