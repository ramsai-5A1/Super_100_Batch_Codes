def isSame(word1, index1, n1, word2, index2, n2):
    if index1 == n1 and index2 == n2:
        return True 
    elif index1 == n1 or index2 == n2:
        return False 
    elif word1[index1] != word2[index2]:
        return False 

    return isSame(word1, index1 + 1, n1, word2, index2 + 1, n2)


word1 = "programming"
word2 = "programming"
result = isSame(word1, 0, len(word1), word2, 0, len(word2))
if result:
    print("Same")
else:
    print("Not same")
