#11. Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

total_amount = 0

ticket_price = float(input("Enter the ticket price per person: "))

for i in range(1, 6):
    age = int(input(f"Enter age of person {i}: "))

    if age < 12:
        amount = ticket_price * 0.7     
    elif age > 59:
        amount = ticket_price * 0.5     
    else:
        amount = ticket_price           
    total_amount += amount

print(f"\nTotal amount to be paid for 5 people: ₹{total_amount}")
