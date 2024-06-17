class Solution(object):
    def goodNodes(self, root):
        result = [0]

        def helper(root, path):
            if not root:
                return 

            path.append(root.val)
            mx = max(path)
            if mx == root.val:
                result[0] += 1 
            helper(root.left, path)
            helper(root.right, path)
            path.pop()

        
        path = []
        helper(root, path)
        return result[0]