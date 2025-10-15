#13. Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill

units = float(input("Enter electricity units consumed: "))

if units <= 50:
    amount = units * 0.50
elif units <= 150:
    amount = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    amount = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    amount = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = amount * 0.20
total_bill = amount + surcharge

print(f"Electricity Bill = ₹{total_bill:.2f}")
