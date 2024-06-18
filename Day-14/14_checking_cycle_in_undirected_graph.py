from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited = [False] * V 
	    def isCyclePresent(node, parent):
	        visited[node] = True 
	        for neighbour in adj[node]:
	            if visited[neighbour] == False:
	                if isCyclePresent(neighbour, node):
	                    return True 
	            elif neighbour != parent:
	                return True 
	        return False
	        
	    for node in range(V):
	        if visited[node] == False:
	            if isCyclePresent(node, -1):
	                return True 
	    return False