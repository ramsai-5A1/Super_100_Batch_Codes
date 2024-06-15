class Solution(object):
    def zigzagLevelOrder(self, root):
        result = []
        if root == None:
            return result
            
        Q = [root]
        level = 0 
        
        while len(Q) > 0:
            n = len(Q)
            subResult = []
            for i in range(n):
                # step-1: popping
                curr = Q.pop(0)
                subResult.append(curr.val)
                
                # step-2: pushing left child if its not none 
                if curr.left != None:
                    Q.append(curr.left)
                
                # step-3: pushing right child if its not none
                if curr.right != None:
                    Q.append(curr.right)
            
            if level % 2 == 1:
                subResult = subResult[::-1]
                
            result.append(subResult)
            level += 1 
        
        #print(result)
        # for subLevel in result:
        #     print(*subLevel) 
        return result
