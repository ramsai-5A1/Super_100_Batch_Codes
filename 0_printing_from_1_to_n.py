def solveIt(index, n):
    if index > n:
        return 

    print(index, end = " ")
    solveIt(index + 1, n)

n = int(input())
solveIt(1, n)
