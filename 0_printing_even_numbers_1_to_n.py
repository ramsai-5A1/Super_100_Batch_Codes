def solveIt(index, n):
    if index > n:
        return 

    print(index, end = " ")
    solveIt(index + 2, n)

n = int(input())
solveIt(2, n)
