#11. WAP to check if given number Strong Number.

num = int(input("Enter a number: "))
temp = num
sum = 0

while(temp > 0):
    digit = temp % 10         
    fact = 1
    for i in range(1, digit + 1):
        fact *= i             
    sum += fact               
    temp //= 10               

if(sum == num):
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")

