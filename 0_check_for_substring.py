def checkSubstring(mainString, index1, n1, subString, index2, n2):
    if index2 == n2:
        return True 
    elif index1 == n1:
        return False 
    elif mainString[index1] != subString[index2] and index2 > 0:
        return checkSubstring(mainString, index1, n1, subString, 0, n2)
    elif mainString[index1] == subString[index2]:
        return checkSubstring(mainString, index1 + 1, n1, subString, index2 + 1, n2)
    return checkSubstring(mainString, index1 + 1, n1, subString, 0, n2)



mainString = "i lloe programming"
subString = "love"
result = checkSubstring(mainString, 0, len(mainString), subString, 0, len(subString))
if result:
    print("Yes, its a substring")
else:
    print("No, its not a substring")
