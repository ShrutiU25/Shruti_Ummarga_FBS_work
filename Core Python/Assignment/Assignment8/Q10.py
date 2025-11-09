#10. Write a program to check if entered year is a leap year or not.

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")
