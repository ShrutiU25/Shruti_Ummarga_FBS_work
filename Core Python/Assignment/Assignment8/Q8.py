#8. Write a program find reverse of a number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10         
        rev = rev * 10 + digit   
        num //= 10              
    return rev

n = int(input("Enter a number: "))
print("Reverse of the number =", reverse_number(n))
