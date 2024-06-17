'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        
        def helper(currNode):
            if not currNode:
                return 
            elif currNode.key == key:
                # Predecessor
                temp = currNode.left 
                while temp and temp.right:
                    temp = temp.right 
                if temp:
                    pre.key = temp.key 
                
                # Successor
                temp = currNode.right 
                while temp and temp.left:
                    temp = temp.left 
                    
                if temp:
                    suc.key = temp.key
                
                return
            elif currNode.key > key:
                suc.key = currNode.key 
                helper(currNode.left)
            else:
                pre.key = currNode.key
                helper(currNode.right)
        helper(root)
            
