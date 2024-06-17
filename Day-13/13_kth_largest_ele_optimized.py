#User function Template for python3

# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        value = [k]
        result = [-1]

        def collectInorderTraversal(currNode):
            if not currNode:
                return 

            collectInorderTraversal(currNode.right)
            value[0] -= 1 
            if value[0] == 0:
                result[0] = currNode.data 
                
            collectInorderTraversal(currNode.left)

        collectInorderTraversal(root)
        return result[0]
