#3. Convert distant given in feet and inches into meter and centimeter.
feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

feet_to_meters = 0.3048       
inches_to_meters = 0.0254     

total_meters = (feet * feet_to_meters) + (inches * inches_to_meters)

meters = int(total_meters)                  
centimeters = (total_meters - meters) * 100 

print(f"{feet} feet and {inches} inches is equal to {meters} meters and {centimeters:.2f} centimeters")
