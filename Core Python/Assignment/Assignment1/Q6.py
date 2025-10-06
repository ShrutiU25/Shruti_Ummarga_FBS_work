#6. Write a Program to input two angles from user and find third angle of the triangle.
angle1 = float(input("Enter the first angle of the triangle: "))
angle2 = float(input("Enter the second angle of the triangle: "))

angle3 = 180 - (angle1 + angle2)

print("The third angle of the triangle is:", angle3)
