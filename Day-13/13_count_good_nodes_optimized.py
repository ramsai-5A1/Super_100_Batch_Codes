class Solution(object):
    def goodNodes(self, root):
        result = [0]

        def helper(root, mxValue):
            if not root:
                return 

            mxValue = max(mxValue, root.val)
            if mxValue == root.val:
                result[0] += 1 
            helper(root.left, mxValue)
            helper(root.right, mxValue)

        
        
        helper(root, -100000)
        return result[0]