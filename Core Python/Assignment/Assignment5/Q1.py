#1. Write a program to prompt user to enter userid and password. 
#If Id andpassword is incorrect give him chance to re-enter the credentials. 
#Let him try 3 times. After that program to terminate.

id = "Srcoe"
password = "1234"

for attempt in range(3):
    user_id = input("Enter User ID: ")
    user_password = input("Enter Password: ")

    if(user_id == id and user_password == password):
        print("Login Successfull")
        break
    else:
        print("Unsuccessfull login")
        print("Attempts left:", 2 - attempt)

else:
    print("Too many failed attempts")        
