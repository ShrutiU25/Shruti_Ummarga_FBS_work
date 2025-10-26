#2. WAP to print all odd numbers until n.

n = int(input("Enter a number till you want the odd numbers: "))

print(f"Odd numbers until {n} :")

for i in range(1, n+1, 2):
    print(i, end=" ")

