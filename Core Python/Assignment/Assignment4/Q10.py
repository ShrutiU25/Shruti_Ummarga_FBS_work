#10. WAP to check if given number is Perfect Number.

n = int(input("Enter a number to check a perfect number: "))
total = 0

for i in range(1,n):
    if(n % i == 0):
     total = total + i

if(total == n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")    