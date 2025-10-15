#7. Write a program to check if user has entered correct userid and password.
user_id = "srcoe123"
password = 1234567

u = input("Enter User ID: ")
p = input("Enter Password: ")

if(u == user_id and p == password):
    print("Login successful!")
elif(u != user_id and p == password):
    print("Incorrect User ID.")
elif(u == user_id and p != password):
    print("Incorrect Password.")
else:
    print("Both User ID and Password are incorrect.")
