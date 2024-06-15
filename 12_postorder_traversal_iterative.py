class Solution(object):
    def postorderTraversal(self, root):
        if root == None:
            return []
            
        result = []
        stack = [[root, 1]]
        while len(stack) > 0:
            curr = stack[-1]
            if curr[1] == 1:
                curr[1] += 1  
                if curr[0].left:
                    stack.append([curr[0].left, 1])
            elif curr[1] == 2:
                curr[1] += 1 
                if curr[0].right:
                    stack.append([curr[0].right, 1])
            else:
                result.append(curr[0].val)
                stack.pop()
        
        
        return result
