class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        result = []
        
        def helper(currNode, path):
            if not currNode:
                return 
            path.append(currNode.data)
            
            if not currNode.left and not currNode.right:
                result.append(path[:])
                path.pop()
                return 
            
            
            helper(currNode.left, path)
            helper(currNode.right, path)
            path.pop()
            
        helper(root, [])
        return result