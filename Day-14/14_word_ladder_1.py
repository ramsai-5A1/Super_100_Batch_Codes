class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return 0 
                
        n = len(beginWord)
        Q = [[beginWord, 1]]
        visited = set()
        visited.add(beginWord)
        
        while Q:
            curr = Q.pop(0)
            if curr[0] == endWord:
                return curr[1]
                
            word = list(curr[0])
            for index in range(n):
                oldChar = word[index]
                for value in range(97, 123):
                    letter = chr(value)
                    word[index] = letter 
                    currWord = "".join(word)
                    if currWord in wordList and currWord not in visited:
                        visited.add(currWord)
                        Q.append([currWord, curr[1] + 1])
                word[index] = oldChar
        return 0
                
            