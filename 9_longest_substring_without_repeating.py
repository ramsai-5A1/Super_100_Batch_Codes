class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        left, right = 0, 0 
        result = 0 
        store = set()
        while right < n:
            while s[right] in store:
                store.remove(s[left])
                left += 1 
            store.add(s[right])
            right += 1 
            result = max(result, len(store))

        return result
        
