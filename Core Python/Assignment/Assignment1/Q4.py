#4. Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter the Principal amount: "))
T = float(input("Enter the Time (in years): "))
R = float(input("Enter the Rate of Interest: "))

SI = (P * T * R) / 100

print("Simple Interest =", SI)
