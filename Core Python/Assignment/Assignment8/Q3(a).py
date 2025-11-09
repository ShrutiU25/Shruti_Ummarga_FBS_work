#3. Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def sum_natural(n):
    total = n * (n + 1) // 2
    return total

n = int(input("Enter value of n: "))
print("Sum of series of numbers: ", sum_natural(n))
