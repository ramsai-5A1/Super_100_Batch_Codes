class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        
        isPresentInPath = [False] * V
        visited = [False] * V 
        
            
        def isCyclePresent(node):
            visited[node] = True
            isPresentInPath[node] = True 
            
            for neighbour in adj[node]:
                if visited[neighbour] == False:
                    if isCyclePresent(neighbour):
                        return True 
                elif isPresentInPath[neighbour]:
                    return True
            
            isPresentInPath[node] = False
            return False
        
        for node in range(V):
            if visited[node] == False:
                if isCyclePresent(node):
                    return True 
        return False