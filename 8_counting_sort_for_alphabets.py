class Solution:
    #Function to arrange all letters of a string in lexicographical 
    #order using Counting Sort.
    def countSort(self,arr):
        
        # as there can be at max a to z alphabets, so taking an list of size 26
        store = [0] * 26 
        
        # calculating frequency for each character by considering a as 0, b as 1, c as 2 and so on
        aAsciiValue = ord('a')
        for ch in arr:
            chAsciiValue = ord(ch) 
            index = chAsciiValue - aAsciiValue
            store[index] += 1 
            
        # prefix sum
        for index in range(1, 26):
            store[index] += store[index - 1]
            
        n = len(arr)
        result = [-1] * n
        # placing each character at its corresponding index
        for index in range(n - 1, -1, -1):
            ch = arr[index]
            chAsciiValue = ord(ch) 
            index = chAsciiValue - aAsciiValue
            store[index] -= 1 
            result[store[index]] = ch
        
        # returning the result in the form of a string
        return "".join(result)
