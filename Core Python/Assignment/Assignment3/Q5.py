#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if(a == b == c):
    print("Triangle is equilateral triangle")
elif(a == b or b == c or c == a):
    print("Triangle is isosceles triangle")
else:
    print("Triangle is scalene")     
