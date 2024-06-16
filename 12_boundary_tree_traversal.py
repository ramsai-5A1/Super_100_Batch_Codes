class Solution:
    def printBoundaryView(self, root):
        if root == None:
           return
       
        def collectLeftView(root, result):
           if root == None or (root.left == None and root.right == None):
               return
          
           result.append(root.data)
           if root.left != None:
               collectLeftView(root.left, result)
           else:
               collectLeftView(root.right, result)
      
        def collectLeaves(root, result):
           if root == None:
               return
          
           if root.left == None and root.right == None:
               result.append(root.data)
               return
          
           collectLeaves(root.left, result)
           collectLeaves(root.right, result)
              
      
        def collectRightView(root, result):
           temp = []
           curr = root
           while curr != None:
               if curr.left == None and curr.right == None:
                   break
               temp.append(curr.data)
               if curr.right != None:
                   curr = curr.right
               else:
                   curr = curr.left
                  
           temp = temp[::-1]
           for ele in temp:
               result.append(ele)
      
        result = []
        if root.left or root.right:
            result.append(root.data)
        collectLeftView(root.left, result)
        collectLeaves(root, result)
        collectRightView(root.right, result)
        return result
