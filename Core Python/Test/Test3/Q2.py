#Q2.Write a program to calculate the sum of following series where n is input by user 
#1/1! + 2/2! + 3/3! + 4/4! + .... N/N!

n = int(input("Enter n: "))
fact = 1
sum_series = 0

for i in range(1, n + 1):
    fact *= i
    sum_series += i / fact

print("Sum of series =", sum_series)
