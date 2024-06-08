def isItPalindrome(word, left, right):
    if left >= right:
        return True 
    elif word[left] != word[right]:
        return False 

    return isItPalindrome(word, left + 1, right - 1)


word = "madama"
result = isItPalindrome(word, 0, len(word) - 1)
if result:
    print("Yes, its a palindrome")
else:
    print("No, its not a palindrome")
