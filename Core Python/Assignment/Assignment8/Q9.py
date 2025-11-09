#9. Write a program to check if entered number is a palindrome or not.

def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev == original

n = int(input("Enter a number: "))

if is_palindrome(n):
    print(n, "is a Palindrome number.")
else:
    print(n, "is not a Palindrome number.")
