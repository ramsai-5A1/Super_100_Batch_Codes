class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True 
        elif not p or not q:
            return False 
        elif p.val != q.val:
            return False 
        
        checkLeftSubtree = self.isSameTree(p.left, q.left)
        checkRightSubtree = self.isSameTree(p.right, q.right)
        return checkLeftSubtree and checkRightSubtree