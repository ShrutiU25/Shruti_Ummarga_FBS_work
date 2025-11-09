#1. Write a program to calculate area of rectangle

def area_of_rectangle(length, breadth):
    area = length * breadth
    return area

l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))

print("Area of rectangle =", area_of_rectangle(l, b))
