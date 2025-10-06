#Q4 Calculate the cost of painting the following building's walls (both interior and exterior).
#You need to accept area(one wall) and cost of both interior and exterior wall 

length_of_interior = int(input("Enter the length interior wall: "))
breadth_of_interior = int(input("Enter the breadth interior wall: "))
cost_for_interior = float(input("Enter the cost per square meter of interior wall: "))

length_of_exterior = int(input("Enter the length exterior wall: "))
breadth_of_exterior = int(input("Enter the breadth exterior wall: "))
cost_for_exterior = float(input("Enter the cost per square meter of exterior wall: "))

area_of_interior_wall = length_of_interior * breadth_of_interior
cost_of_interior_wall = area_of_interior_wall * cost_for_interior
total_cost_interior = 2 * cost_of_interior_wall

area_of_exterior_wall = length_of_exterior * breadth_of_exterior
cost_of_exterior_wall = area_of_exterior_wall * cost_for_exterior
total_cost_exterior = 2 * cost_of_exterior_wall

total_cost = total_cost_exterior + total_cost_interior

print(f"Total cost {total_cost}: ")