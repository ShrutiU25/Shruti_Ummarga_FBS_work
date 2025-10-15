#12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))

rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)

if num == rev:
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")
