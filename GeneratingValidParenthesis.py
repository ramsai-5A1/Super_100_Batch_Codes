class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def findAllValidOnes(left, right, path):
            if left < right:
                return
            if left + right == 2 * n:
                result.append("".join(path))
                return

            if left < n:
                path.append("(")
                findAllValidOnes(left + 1, right, path)
                path.pop()

            if right < n:
                path.append(")")
                findAllValidOnes(left, right + 1, path)
                path.pop()
        path = []
        findAllValidOnes(0, 0, path)
        return result
        
