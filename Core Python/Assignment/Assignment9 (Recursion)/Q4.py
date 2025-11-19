#4. Write a program to find sum of n numbers using recursion.

def sumOfSeries(n):
    if(n <= 0):
        return 0
    else:
        return n + sumOfSeries(n - 1)
    
n = int(input("Enter value for sum of series: "))
result = sumOfSeries(n)
print("Output:",result)    