#3. Write a program to find sum of following series using functions :
#b. 1!+ 2! + 3! + 4!+..... + n!

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sum_factorial_series(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total

n = int(input("Enter value of n: "))
print("Sum of series of factorial =", sum_factorial_series(n))

