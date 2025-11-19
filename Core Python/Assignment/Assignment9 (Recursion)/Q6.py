#6. Write a program to print Fibonacci series using recursion.

def fib(n):
    if(n <= 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter number of terms: "))
for i in range(n):
    print(fib(i), end = " ")
