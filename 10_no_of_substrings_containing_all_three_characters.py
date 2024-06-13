class Solution(object):
    def numberOfSubstrings(self, s):
        store = dict()
        store['a'] = 0 
        store['b'] = 0 
        store['c'] = 0 
        left, right = 0, 0 
        n = len(s)
        result = 0
        while right < n:
            store[s[right]] += 1 
            while store['a'] > 0 and store['b'] > 0 and store['c'] > 0:
                result += (n - right)
                store[s[left]] -= 1 
                left += 1
            right += 1 
        return result
        
