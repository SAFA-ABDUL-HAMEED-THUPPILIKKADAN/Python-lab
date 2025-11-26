rows = int(input("Enter the number of rows: "))

cols = int(input("Enter the number of cols: "))

matrix = []


for i in range(rows):
    row = []

    for j in range(cols):
        value = int(input(f"Enter the value matrix[{i}][{j}]:"))
        row.append(value)
    matrix.append(row)


# for r in matrix:
#     print(r)


rows1 = int(input("Enter the number of rows: "))

cols1 = int(input("Enter the number of cols: "))

matrix1 = []


for i in range(rows1):
    row1 = []

    for j in range(cols1):
        value = int(input(f"Enter the value matrix[{i}][{j}]:"))
        row1.append(value)
    matrix1.append(row1)


matrix2 = []


for i in range(rows1):
    row2 = []

    for j in range(cols1):
        row2.append(matrix[i][j]+matrix1[i][j])
    matrix2.append(row2)


for r1 in matrix2:
    print(r1)


# for i in range(cols):
#     for j in range(rows):
#         print(matrix[j][i], end=" ")
#     print()
