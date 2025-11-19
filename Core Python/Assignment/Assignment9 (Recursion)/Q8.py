#8. Write a program to check whether a number is prime or not using recursion.

def is_prime(n, i = 2):
    if(n <= 1):
        return False
    elif(i * i > n):
        return True
    elif(n % i == 0):
        return False
    else:
        return is_prime(n, i + 1)

n = int(input("Enter number: "))

if is_prime(n):
    print("Prime Number")
else:
    print("Not Prime")
