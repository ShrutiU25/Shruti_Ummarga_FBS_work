#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if gender == "male":
    if age >= 21:
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
elif gender == "female":
    if age >= 18:
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
else:
    print("Invalid gender entered.")
