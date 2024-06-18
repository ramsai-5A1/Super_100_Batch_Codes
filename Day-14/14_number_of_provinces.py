class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        result = 0 
        visited = [False] * n

        def visitAllAdjacentNodes(node):
            visited[node] = True 
            Q = [node]

            while Q:
                curr = Q.pop(0)
                for neighbour in range(n):
                    if isConnected[curr][neighbour] == 1 and visited[neighbour] == False:
                        visited[neighbour] = True 
                        Q.append(neighbour)

        for node in range(n):
            if visited[node] == False:
                visitAllAdjacentNodes(node)
                result += 1
        return result