#7. Write a program to find sum of digits using recursion.

def sumOfDigit(num):
    if(num <= 0):
        return 0
    else:
        return(num % 10) + sumOfDigit(num // 10)
    
n = int(input("Enter number: "))
print(sumOfDigit(n))    