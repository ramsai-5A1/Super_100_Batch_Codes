class Solution(object):
    def divideAllSubStrings(self, index, word, wordDict, cache):
        if index == len(word):
            return True
        if cache[index] != -1:
            if cache[index] == 1:
                return True 
            return False
        
        currentWord = ""
        for position in range(index, len(word)):
            currentWord += word[position]
            # Below we are trying to check whether the substring is a palindrome or not
            if currentWord in wordDict:
                nextResult = self.divideAllSubStrings(position + 1, word, wordDict, cache)
                if nextResult == True:
                    cache[index] = 1
                    return True 
        cache[index] = 0
        return False

    def wordBreak(self, s, wordDict):
        tempDict = list(set(wordDict))
        cache = [-1] * (len(s))
        return self.divideAllSubStrings(0, s, tempDict, cache)
