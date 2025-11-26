def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def print_fib_series(count):
    for i in range(count):
        print(fib(i), end=" ")


# Example: Print first 10 Fibonacci numbers
num = int(input("Enter how many terms you want: "))
print_fib_series(num)
