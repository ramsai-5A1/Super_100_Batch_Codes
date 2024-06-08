class Solution:
    def toh(self, N, fromm, to, aux):
        result = [0]
        
        def solveIt(N, fromm, to, aux):
            if N == 1:
                print("move disk 1 from rod", fromm, "to rod", to)
                result[0] += 1
                return 
            solveIt(N - 1, fromm, aux, to)
            print("move disk", N, "from rod", fromm, "to rod", to)
            result[0] += 1
            solveIt(N - 1, aux, to, fromm)
            
        solveIt(N, fromm, to, aux)
        return result[0]
