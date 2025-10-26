#1. Write a program to accept year from user and check if it is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year ")
else:
    print(year, "is Not a Leap Year ")
