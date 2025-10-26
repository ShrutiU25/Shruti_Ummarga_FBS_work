#1. WAP to print all even numbers until n.

n = int(input("Enter a number till you want the even numbers: "))

print(f"Even numbers until {n} :")

for i in range(2, n+1, 2):
    print(i, end=" ")
