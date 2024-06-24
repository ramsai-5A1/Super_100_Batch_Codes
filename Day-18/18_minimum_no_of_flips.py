class Solution(object):
    def minBitFlips(self, start, goal):
        result = 0 
        for i in range(31):
            a = start & (1 << i)
            b = goal & (1 << i)
            if a != b:
                result += 1
        return result