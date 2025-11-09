#2. Write a program to calculate area of circle

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

r = float(input("Enter radius of the circle: "))
print("Area of circle =", area_of_circle(r))
