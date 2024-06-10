class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self, n, m, str1, str2):
        
        def recursiveApproach(index1, index2):
            if index1 == n or index2 == m:
                return 0 
            elif str1[index1] == str2[index2]:
                return 1 + recursiveApproach(index1 + 1, index2 + 1)
            
            choice1 = recursiveApproach(index1 + 1, index2)
            choice2 = recursiveApproach(index1, index2 + 1)
            return max(choice1, choice2)
            
        cache = [[-1] * m for i in range(n)]
        
        def memoizationApproach(index1, index2):
            if index1 == n or index2 == m:
                return 0 
            elif cache[index1][index2] != -1:
                return cache[index1][index2]
            elif str1[index1] == str2[index2]:
                cache[index1][index2] = 1 + memoizationApproach(index1 + 1, index2 + 1)
                return cache[index1][index2]
            
            choice1 = memoizationApproach(index1 + 1, index2)
            choice2 = memoizationApproach(index1, index2 + 1)
            cache[index1][index2] = max(choice1, choice2)
            return cache[index1][index2]
            
            
        def tabulationApproach():
            cache = [[0] * (m + 1) for i in range(n + 1)]
            for index1 in range(n - 1, -1, -1):
                for index2 in range(m - 1, -1, -1):
                    if str1[index1] == str2[index2]:
                        cache[index1][index2] = 1 + cache[index1 + 1][index2 + 1]
                    else:
                        choice1 = cache[index1 + 1][index2]
                        choice2 = cache[index1][index2 + 1]
                        cache[index1][index2] = max(choice1, choice2)
                    
            return cache[0][0]
            
        return tabulationApproach()
