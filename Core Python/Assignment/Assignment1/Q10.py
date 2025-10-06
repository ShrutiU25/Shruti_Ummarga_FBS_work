#10. Write a program to calculate area of an equilateral triangle.
import math  
side = float(input("Enter the side of the equilateral triangle: "))

area = (math.sqrt(3) / 4) * (side ** 2)
print("The area of the equilateral triangle is:", area)
