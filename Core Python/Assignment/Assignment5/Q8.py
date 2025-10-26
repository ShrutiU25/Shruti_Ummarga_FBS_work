#8. Write a program to solve the following series :

#a. 1! + 2! + 3! + 4! + .....n!
import math

n = int(input("Enter n: "))
sum_factorial = 0

for i in range(1, n + 1):
    sum_factorial += math.factorial(i)

print("Sum of series 1! + 2! + ... +", n, "! =", sum_factorial)

#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
n = int(input("Enter N: "))
sum_power = 0

for i in range(1, n + 1):
    sum_power += n ** i

print("Sum of series N + N^2 + ... + N^N =", sum_power)

#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter n (number of terms): "))
sum_geo = 0
ratio = 2

for i in range(n):
    sum_geo += ratio ** i  

print("Sum of geometric series =", sum_geo)

#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = float(input("Enter value of a: "))
sum_series = 0

for i in range(1, 11):
    sum_series += (a ** i) / i

print("Sum of the series S =", sum_series)

#e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))
sum_series = 0

for i in range(1, n + 1):
    term = (x ** i) / (2 * i - 1)
    if i % 2 == 0:
        term = -term  
    sum_series += term

print("Sum of the series =", sum_series)
