class Solution(object):
    def distanceK(self, root, target, k):
        result = []

        def addAllKSeperated(currNode, distance):
            if distance > k or not currNode:
                return 
            elif distance == k:
                result.append(currNode.val)
                return 
            addAllKSeperated(currNode.left, distance + 1)
            addAllKSeperated(currNode.right, distance + 1)


        def helper(currNode):
            if not currNode:
                return [False, -1]
            if currNode.val == target.val:
                addAllKSeperated(currNode, 0)
                return [True, 1]
                
            leftVal = helper(currNode.left)
            if leftVal[0]:
                if leftVal[1] == k:
                    result.append(currNode.val)
                else:
                    addAllKSeperated(currNode.right, leftVal[1] + 1)
                return [True, leftVal[1] + 1]

            rightVal = helper(currNode.right)
            if rightVal[0]:
                if rightVal[1] == k:
                    result.append(currNode.val)
                else:
                    addAllKSeperated(currNode.left, rightVal[1] + 1)
                return [True, rightVal[1] + 1]

            return [False, -1]


        helper(root)
        return result