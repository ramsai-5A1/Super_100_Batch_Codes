def printMatrix(row, col, matrix, n):
    if row == -1:
        return 

    print(matrix[row][col], end = " ")
    if col == 0:
        print()
        printMatrix(row - 1, n - 1, matrix, n)
    else:
        printMatrix(row, col - 1, matrix, n)


matrix = []
for i in range(1, 5):
    row = []
    for j in range(1, 10):
        row.append(j)
    matrix.append(row)

m = len(matrix)
n = len(matrix[0])
printMatrix(m - 1, n - 1, matrix, n)
