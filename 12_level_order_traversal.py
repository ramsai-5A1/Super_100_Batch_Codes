class Solution(object):
    def levelOrder(self, root):
        result = []
        if root == None:
            return result

        Q = []
        Q.append(root)

        while Q:
            n = len(Q)
            subResult = []
            for i in range(n):
                current = Q.pop(0)
                subResult.append(current.val)

                if current.left != None:
                    Q.append(current.left)

                if current.right != None:
                    Q.append(current.right)

            result.append(subResult)
        return result
