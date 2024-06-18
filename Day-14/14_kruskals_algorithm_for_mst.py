


class DSU:
    def __init__(self, V):
        self.V = V 
        self.parent = [-1] * V 
        self.size = [1] * V
        
    def getParent(self, a):
        if self.parent[a] == -1:
            return a 
        self.parent[a] = self.getParent(self.parent[a])
        return self.parent[a]
        
    def mergeThese(self, a, b):
        aParent = self.getParent(a)
        bParent = self.getParent(b)
        if aParent == bParent:
            return False 
        
        if self.size[aParent] > self.size[bParent]:
            self.size[aParent] += self.size[bParent]
            self.parent[bParent] = aParent 
        else:
            self.size[bParent] += self.size[aParent]
            self.parent[aParent] = bParent
            
        
        return True



class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        result = 0 
        edges = []
        for node in range(V):
            for edge in adj[node]:
                edges.append([edge[1], node, edge[0]])
                
        edges.sort()
        obj = DSU(V)
        edgesToInclude = V - 1 
        while edgesToInclude > 0:
            currentEdge = edges.pop(0)
            
            # Only if successfull merge happened, then only we are adding to result and decrementing the edgesCount
            if obj.mergeThese(currentEdge[1], currentEdge[2]):
                result += currentEdge[0]
                edgesToInclude -= 1
        
        return result
