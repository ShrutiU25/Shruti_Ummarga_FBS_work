#6. Write a program to calculate profit or loss.
cost_price = float(input("Enter the cost price:"))
selling_price = float(input("Enter the selling price:"))

if(selling_price > cost_price):
    print("Profit")
elif(selling_price < cost_price):
    print("Loss")    
else:
    print("Neither profit nor loss")    