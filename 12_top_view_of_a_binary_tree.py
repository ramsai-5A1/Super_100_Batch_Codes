#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    
    def solveIt(self, root, store, level, hd):
        if root == None:
            return 
        
        if hd not in store or store[hd][0] > level:
            store[hd] = [level, root.data]
        self.solveIt(root.left, store, level + 1, hd - 1)
        self.solveIt(root.right, store, level + 1, hd + 1)
    
    def topView(self,root):
        result = []
        if root == None:
            return result
            
        store = {}
        self.solveIt(root, store, 0, 0)
        temp = store.keys()
        temp = sorted(temp)
        for curr in temp:
            result.append(store[curr][1])
        return result
        
        # code here
