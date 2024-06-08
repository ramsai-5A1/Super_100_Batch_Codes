class Solution(object):

    def printAllPartitions(self, index, word, result, path):
        if index == len(word):
            result.append(path[:])
            return
        
        
        currentWord = ""
        for position in range(index, len(word)):
            currentWord += word[position]
            # Below we are trying to check whether the substring is a palindrome or not
            if currentWord == currentWord[::-1]:
                path.append(currentWord)
                self.printAllPartitions(position + 1, word, result, path)
                path.pop()

    def partition(self, s):
        result = []
        path = []
        self.printAllPartitions(0, s, result, path)
        return result
        
