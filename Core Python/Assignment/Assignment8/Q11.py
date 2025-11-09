#11. WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

def is_armstrong(num):
    n = num
    digits = count_digits(num)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10
    return total == num

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
