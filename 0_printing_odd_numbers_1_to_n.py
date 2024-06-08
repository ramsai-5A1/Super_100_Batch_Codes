def solveIt(index, n):
    if index > n:
        return 

    print(index, end = " ")
    solveIt(index + 2, n)

n = int(input())
solveIt(1, n)
