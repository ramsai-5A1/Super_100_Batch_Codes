# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
    
        def findPath(currRoot, value, path):
            if not currRoot:
                return False 
            
            path.append(currRoot)
            if currRoot.val == value.val:
                return True

            isFoundInLeftSubtree = findPath(currRoot.left, value, path)
            if isFoundInLeftSubtree:
                return True 

            
            isFoundInRightSubtree = findPath(currRoot.right, value, path)
            if isFoundInRightSubtree:
                return True 

            path.pop()
            return False
            
            


        path1 = []
        findPath(root, p, path1)
        path2 = []
        findPath(root, q, path2)
        result = None 
        index = 0 
        while index < min(len(path1), len(path2)):
            if path1[index].val == path2[index].val:
                result = path1[index]
            else:
                break 
            index += 1

        return result