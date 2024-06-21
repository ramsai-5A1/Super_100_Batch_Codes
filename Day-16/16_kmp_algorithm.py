class Solution:
    def search(self, pat, txt):
        n, m = len(txt), len(pat)
        lps = [0] * m 
        mainIndex, patIndex = 1, 0 
        while mainIndex < m:
            if pat[mainIndex] == pat[patIndex]:
                lps[mainIndex] = patIndex + 1 
                mainIndex += 1 
                patIndex += 1 
            else:
                if patIndex > 0:
                    patIndex = lps[patIndex - 1]
                else:
                    mainIndex += 1 
                    
        txtIndex, patIndex = 0, 0 
        result = []
        while txtIndex < n:
            if pat[patIndex] == txt[txtIndex]:
                patIndex += 1 
                txtIndex += 1 
                if patIndex == m:
                    result.append(txtIndex - m + 1)
                    patIndex = lps[patIndex - 1]
            else:
                if patIndex > 0:
                    patIndex = lps[patIndex - 1]
                else:
                    txtIndex += 1 
        return result