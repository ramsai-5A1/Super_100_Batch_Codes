class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        
        result = [1]
        def helper(currNode):
            if not currNode:
                return 0 
            elif not currNode.left and not currNode.right:
                return currNode.data 
                
            leftValue = helper(currNode.left)
            rightValue = helper(currNode.right)
            if currNode.data != (leftValue + rightValue):
                result[0] = 0 
            return currNode.data
                
        
        helper(root)
        return result[0]