class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
            
        result = []
        stack = [[root, 1]]
        while len(stack) > 0:
            curr = stack[-1]
            if curr[1] == 1:
                result.append(curr[0].val)
                curr[1] += 1  
                if curr[0].left:
                    stack.append([curr[0].left, 1])
            elif curr[1] == 2:
                curr[1] += 1 
                if curr[0].right:
                    stack.append([curr[0].right, 1])
            else:
                stack.pop()
        
        
        return result
