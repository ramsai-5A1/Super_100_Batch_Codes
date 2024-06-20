class TrieNode:
    def __init__(self):
        self.isEnd = False 
        self.passing = 0 
        self.store = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def getRoot(self):
        return self.root 

    def insertIntoTrie(self, word):
        currNode = self.root 
        currNode.passing += 1 
        for ch in word:
            if ch not in currNode.store:
                currNode.store[ch] = TrieNode() 
            currNode = currNode.store[ch]
            currNode.passing += 1 
        currNode.isEnd = True 

    def removeFromTrie(self, word):
        currNode = self.root 
        currNode.passing -= 1 
        for ch in word:
            currNode = currNode.store[ch]
            currNode.passing -= 1 
        currNode.isEnd = False 



class Solution(object):
    def findWords(self, board, words):
        obj = Trie()
        for word in words:
            obj.insertIntoTrie(word)

        result = []
        n, m = len(board), len(board[0])
        root = obj.getRoot()

        def helper(row, col, letters, currNode):
            if currNode.passing <= 0:
                return
            elif board[row][col] not in currNode.store:
                return 

            ch = board[row][col]
            currNode = currNode.store[ch]
            letters.append(ch)
            if currNode.isEnd:
                word = "".join(letters)
                result.append(word)
                obj.removeFromTrie(word)
            

            
            board[row][col] = '#'

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if min(newRow, newCol) < 0 or newRow >= n or newCol >= m or board[newRow][newCol] == '#':
                    continue 

                helper(newRow, newCol, letters, currNode)


            board[row][col] = ch 
            letters.pop()


        for row in range(n):
            for col in range(m):
                letters = []
                helper(row, col, letters, root)
        return result