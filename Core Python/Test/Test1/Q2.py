#Q2 Write a program to calculate simple interest based on principal,rate,and time (SI=P*R*T/100)
P = float(input("Enter the Principal amount: "))
T = float(input("Enter the Time (in years): "))
R = float(input("Enter the Rate of Interest: "))

SI = (P * T * R) / 100

print("Simple Interest =", SI)
