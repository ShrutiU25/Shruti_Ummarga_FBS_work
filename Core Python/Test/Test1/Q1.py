#Q1 Write a program to find the area and perimeter of following figure (accept length,breadth,radius from user)
l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
r = int(input("Enter the radius: "))

area_of_rect = l*b
half_area_of_circle = (3.14 * r **2)/2

perimeter_of_rect = 2 * (l + b)
half_perimeter_of_circle = (2 * 3.14 * r)/2

total_area = area_of_rect + half_area_of_circle
print(f"Total area of the figure is {total_area}.")

total_perimeter = perimeter_of_rect + half_perimeter_of_circle
print(f"Total perimeter of the figure is {total_perimeter}.")


