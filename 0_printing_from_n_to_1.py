def solveIt(index):
    if index == 0:
        return 

    print(index, end = " ")
    solveIt(index - 1)

n = int(input())
solveIt(n)
