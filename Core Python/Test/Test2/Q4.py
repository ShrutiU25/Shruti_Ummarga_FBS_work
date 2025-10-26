#4. Write a program to calculate the total cost of painting.
#The interior of building with four equal sized walls.

l = float(input("Enter length of wall: "))
h = float(input("Enter height of wall: "))
cost = float(input("Enter cost of painting per square meter(in Rs): "))

total_area = 4 * (l * h)

total_cost = total_area * cost

print(f"\nTotal area to be painted is {total_area} sq.m")
print(f"Total painting cost: Rs.{total_cost}")
