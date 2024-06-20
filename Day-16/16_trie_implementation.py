class TrieNode:
    def __init__(self):
        self.isEnding = False 
        self.store = dict()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insertWord(self, word):
        currRoot = self.root 
        n = len(word)
        for index in range(n):
            if word[index] not in currRoot.store:
                currRoot.store[word[index]] = TrieNode()
            
            currRoot = currRoot.store[word[index]]
        currRoot.isEnding = True 
        print(word, "inserted successfully in the trie")
            
            
    
    def searchWord(self, word):
        currNode = self.root 
        n = len(word)
        for index in range(n):
            ch = word[index]
            if ch not in currNode.store:
                return False 
                
            currNode = currNode.store[ch]
        return currNode.isEnding
        
    
    def startsWith(self, word):
        currNode = self.root 
        n = len(word)
        for index in range(n):
            ch = word[index]
            if ch not in currNode.store:
                return False 
                
            currNode = currNode.store[ch]
        return True
    
obj = Trie()
obj.insertWord("cat")
obj.insertWord("computer")
obj.insertWord("compute")

print(obj.startsWith("com"))
print(obj.startsWith("comput"))
print(obj.startsWith("coma"))

# if obj.searchWord("cat"):
#     print("cat is present in trie")
# else:
#     print("cat is not present in trie")
    
    
# if obj.searchWord("compute"):
#     print("compute is present in trie")
# else:
#     print("compute is not present in trie")