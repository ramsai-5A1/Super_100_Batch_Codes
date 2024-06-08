def checkSubsequence(mainString, index1, n1, subString, index2, n2):
    if index2 == n2:
        return True 
    elif index1 == n1:
        return False 
    elif mainString[index1] == subString[index2]:
        return checkSubsequence(mainString, index1 + 1, n1, subString, index2 + 1, n2)
    return checkSubsequence(mainString, index1 + 1, n1, subString, index2, n2)



mainString = "i llove programming"
subString = "lvpgrmmg"
result = checkSubsequence(mainString, 0, len(mainString), subString, 0, len(subString))
if result:
    print("Yes, its a subsequence")
else:
    print("No, its not a subsequence")
