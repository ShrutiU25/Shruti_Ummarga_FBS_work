#10. Write a program to reverse three-digit number.
num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num % 100) // 10
units = num % 10

reversed_num = (units * 100) + (tens * 10) + hundreds
print("The reversed number is:", reversed_num)
