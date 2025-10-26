#12. WAP to print Armstrong number within a given range

start_num = int(input("Enter start of range: "))
end_num = int(input("Enter end of range: "))

print("Armstrong numbers in the range:")

for num in range(start_num, end_num+ 1):
    digits = len(str(num))
    sum = 0
    temp = num

    while(temp > 0):
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    
    if(sum == num):
        print(num)