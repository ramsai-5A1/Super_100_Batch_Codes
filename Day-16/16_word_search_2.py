
class TrieNode:
    def __init__(self):
        self.isEnding = False 
        self.store = dict()
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def getRoot(self):
        return self.root
 
    def insertWord(self, word):
        currRoot = self.root 
        n = len(word)
        for index in range(n):
            if word[index] not in currRoot.store:
                currRoot.store[word[index]] = TrieNode()
 
            currRoot = currRoot.store[word[index]]
        currRoot.isEnding = True 







class Solution(object):
    def findWords(self, board, words):
        obj = Trie()
        for word in words:
            obj.insertWord(word)
         
        m, n = len(board), len(board[0])
        result = []
        
        def helper(currNode, row, col, path):
            ch = board[row][col] 
            
            if ch not in currNode.store:
                return
            path.append(ch)
            currNode = currNode.store[ch]
            if currNode.isEnding:
                result.append("".join(path[:]))
                currNode.isEnding = False
                
            
            board[row][col] = "#"
            
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n and board[newRow][newCol] != "#":
                    helper(currNode, newRow, newCol, path)
                
            
            board[row][col] = ch
            path.pop()
            
            
            
        
        root = obj.getRoot()
        for row in range(m):
            for col in range(n):
                helper(root, row, col, [])
                
        return result
        