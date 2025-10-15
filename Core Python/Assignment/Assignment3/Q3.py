#3. Write a program to input angles of a triangle and check whether triangle is valid or not.
angle_1 = float(input("Enter the first angle: "))
angle_2 = float(input("Enter the second angle: "))
angle_3 = float(input("Enter the third angle: "))

sum_of_angles = angle_1 + angle_2 + angle_3

if(sum_of_angles == 180):
    print("It is a triangle")
else:
    print("It is not a triangle")    