#9. Write a program to calculate the m to the power n using recursion.

def power(m, n):
    if(n == 0):
        return 0
    else:
        return m * power(m, n - 1)

m = int(input("Enter m: "))
n = int(input("Enter n: "))
print("Result =", power(m, n))
