#7. Write a program to print first n prime numbers.

n = int(input("Enter how many first prime numbers you want: "))

count = 0 
num = 2

while(count < n):
    print("\n Num is:", num)
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        print(num, end='')    
        count += 1
    num += 1    