n = int(input("Enter the range to print triangle: "))

for i in range(1, n + 1):

    for k in range(n - i):
        print(" ", end="")

    for j in range(1, i+1):
        print(j, end=" ")
    print()
