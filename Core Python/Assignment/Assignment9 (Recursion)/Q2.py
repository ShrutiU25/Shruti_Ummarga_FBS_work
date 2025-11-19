#2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrong(num, power):
    if(num == 0):
        return 0
    else:
        return (num % 10) ** power + armstrong(num // 10, power)

n = int(input("Enter a number: "))
digits = len(str(n))

if(armstrong(n, digits) == n):
    print("Armstrong Number")
else:
    print("Not Armstrong")
