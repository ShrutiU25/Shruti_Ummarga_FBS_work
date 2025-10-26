#3. A farmer has a field which is half in circle shape and rest rectangle. 
#He needs to do fencing for entire field using barbed wire 5 times. 
#Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. 
#If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

r = 20 
l = 50
b = 40
cost = 35

peri_cir = 3.14 * r
peri_rec = 2 * (l + b)

total_peri = (peri_cir + peri_rec) * 5
total_cost = 35 * total_peri

print(f"Total perimeter is {total_peri}: ")
print(f"Total cost is {total_cost}: ")
