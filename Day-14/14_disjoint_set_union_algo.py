
# Program that implements Disjoin-Set-Union Algorithm

class DSU:
    def __init__(self, V):
        self.V = V 
        self.parent = [-1] * (V + 1)
        self.size = [1] * (V + 1)
        
    def getParent(self, a):
        if self.parent[a] == -1:
            return a 
            
        # Below single line of code is to improve the performance
        # We are memoizing the result, so that next time it will not recalculate the parent again and again 
        self.parent[a] = self.getParent(self.parent[a])
        return self.parent[a] 
        
    def canWeAddThisEdge(self, a, b):
        aParent = self.getParent(a)
        bParent = self.getParent(b)
        
        # Checking whether both parents are equal, if yes, then there is a possibility that this edge introduce cycle
        if aParent == bParent:
            return False 
        return True 
        
    def addThisEdge(self, a, b):
        aParent = self.getParent(a)
        bParent = self.getParent(b)
        
        # If we can't add this edge, then we are returning back false 
        if aParent == bParent:
            return False 
            
            
        # Incase if that edge is not introducing any cycle, then we are adding that edge 
        # we are doing this on the basis of size, whichever node is having bigger size, we are merging the other node 
        # under the bigger node, it just improves the performance 
        
        
        if self.size[aParent] > self.size[bParent]:
            self.size[aParent] += self.size[bParent]
            self.parent[bParent] = aParent 
        else:
            self.size[bParent] += self.size[bParent]
            self.parent[aParent] = bParent  
            
        # Finally after merging, we are returning back true, saying that we have successfully merged this edge.
        return True 
            
       
# Creating object for Disjoin-Set-Union (DSU) class      
obj = DSU(5)

# Just inserting few edges 
if obj.addThisEdge(0, 3):
    print("Added 0 -- 3 edge")

if obj.addThisEdge(0, 4):
    print("Added 0 -- 4 edge")
    
# Checking whether we can add 3 to 4 edge or not
    
if obj.canWeAddThisEdge(3, 4):
    print("Yes we can add 3 -- 4 edge")
else:
    print("No we can't add 3 -- 4 edge, its introducing cycle")
    
    
if obj.addThisEdge(3, 4):
    print("Added 3 -- 4 edge")
else:
    print("Did not added 3 -- 4 edge")
    
    
    
    
    
    
    
    
    
            
            