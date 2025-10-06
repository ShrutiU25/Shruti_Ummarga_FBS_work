#5. Write a program to enter P, T, R and calculate Compound Interest.
P = float(input("Enter the Principal amount: "))
T = float(input("Enter the Time (in years): "))
R = float(input("Enter the Rate of Interest: "))

A = P * (1 + R / 100) ** T   
CI = A - P                   

print("Compound Interest =", CI)
print("Total Amount =", A)
