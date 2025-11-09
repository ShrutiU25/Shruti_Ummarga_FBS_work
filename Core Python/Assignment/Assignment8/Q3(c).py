#3. Write a program to find sum of following series using functions :
#c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_power_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter value of n: "))
print("Sum of series of power series =", sum_power_series(n))
