#8. Write a program to swap two numbers using third variable.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Before swapping: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)
