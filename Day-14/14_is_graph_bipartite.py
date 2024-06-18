class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        group = [-1] * n 

        def isPossibleToDivide(node, groupId):
            # Group-id denotes either 1 or 2, so that each node can be assigned to either group-1 or group-2. 
            group[node] = groupId 
            for neighbour in graph[node]:
                if group[neighbour] == -1:
                    if isPossibleToDivide(neighbour, 3 - groupId) == False:
                        return False 
                elif group[neighbour] == groupId:
                    return False 
            return True

        for node in range(n):
            if group[node] == -1:
                if isPossibleToDivide(node, 1) == False:
                    return False 
        return True