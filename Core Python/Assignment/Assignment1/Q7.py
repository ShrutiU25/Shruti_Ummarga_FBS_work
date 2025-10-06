#7. Program to Find the Roots of a Quadratic Equation
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = (b ** 2) - (4 * a * c)**0.5
print(f"The roots are -+ {d}")
