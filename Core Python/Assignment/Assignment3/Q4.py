#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if(a + b > c):
    print("Triangle is valid")
elif(a + c > b):
    print("Triangle is valid")
elif(b + c > a):
    print("Triangle is valid") 
else:
    print("Triangle is not valid")    



