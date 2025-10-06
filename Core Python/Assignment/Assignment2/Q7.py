#7. Find the sum of three-digit number.
num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num % 100) // 10
units = num % 10

sum_of_digits = hundreds + tens + units
print("The sum of the digits is:", sum_of_digits)
