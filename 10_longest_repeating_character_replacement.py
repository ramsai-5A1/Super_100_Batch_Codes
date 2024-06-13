class Solution(object):
    def characterReplacement(self, s, k):
        result = 0
        n = len(s)

        def replaceCh(ch):
            left, right = 0, 0 
            remainingTimes = 0
            result = 0
            while right < n:
                if s[right] != ch:
                    if remainingTimes < k:
                        remainingTimes += 1 
                    else:
                        while remainingTimes == k:
                            if s[left] != ch:
                                remainingTimes -= 1 
                            left += 1 
                        remainingTimes += 1 
                result = max(result, right - left + 1)
                right += 1 
            return result


        for value in range(65, 91):
            ch = chr(value)
            result = max(result, replaceCh(ch))
        return result
