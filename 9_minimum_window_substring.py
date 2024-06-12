class Solution(object):
    def minWindow(self, s, t):
        m, n = len(s), len(t)
        tStore = dict() 
        for ch in t:
            if ch not in tStore:
                tStore[ch] = 1 
            else:
                tStore[ch] += 1 

        left, right = 0, 0 
        foundChar = 0 
        neededChar = len(tStore)
        sStore = dict()
        oldOne = m + 1 
        startingIndex = -1 

        while right < m:
            if s[right] not in sStore:
                sStore[s[right]] = 1 
            else:
                sStore[s[right]] += 1 

            if s[right] in tStore and tStore[s[right]] == sStore[s[right]]:
                foundChar += 1 
                while foundChar == neededChar:
                    if right - left + 1 < oldOne:
                        oldOne = right - left + 1 
                        startingIndex = left

                    sStore[s[left]] -= 1 
                    if s[left] in tStore and tStore[s[left]] > sStore[s[left]]:
                        foundChar -= 1 
                        left += 1 
                        break 
                    left += 1 
            right += 1
                

        if startingIndex != -1:
            return s[startingIndex:startingIndex + oldOne]
        return ""
