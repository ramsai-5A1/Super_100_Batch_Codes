class TrieNode:
    def __init__(self):
        self.isEnd = False 
        self.store = dict()


class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word):
        currNode = self.root 
        for ch in word:
            if ch not in currNode.store:
                currNode.store[ch] = TrieNode()
            currNode = currNode.store[ch]
        currNode.isEnd = True
        

    def search(self, word):
        currNode = self.root 
        for ch in word:
            if ch not in currNode.store:
                return False
            currNode = currNode.store[ch]
        return currNode.isEnd
        

    def startsWith(self, prefix):
        currNode = self.root 
        for ch in prefix:
            if ch not in currNode.store:
                return False 
            currNode = currNode.store[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)