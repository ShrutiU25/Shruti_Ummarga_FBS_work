#9. Write a program to swap two numbers without using third variable.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("Before swapping: a =", a, ", b =", b)

a, b = b, a
print("After swapping: a =", a, ", b =", b)
