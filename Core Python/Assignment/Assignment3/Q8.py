##8. Write a program to prompt user to enter userid and password. 
#After verifying userid and password display a 4 digit random number and ask user to enter the same.
#If user enters the same number then show him success message otherwisefailed. (Something like captcha)

import random

userid = "admin"
password = "12345"

u = input("Enter User ID: ")
p = input("Enter Password: ")

if u == userid and p == password:
    
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    
    user_input = int(input("Enter the captcha number shown above: "))
    
    if user_input == captcha:
        print("Login successful! Verification complete.")
    else:
        print("Verification failed! Captcha did not match.")
else:
    print("Invalid User ID or Password.")
