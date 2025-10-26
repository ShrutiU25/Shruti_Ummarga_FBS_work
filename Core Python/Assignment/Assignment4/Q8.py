#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

start_num = int(input("Enter start of range: "))
end_num = int(input("Enter end of range: "))

print("Numbers divisible by 7 and multiple of 5 in range:")

for i in range(start_num, end_num+1):
    if(i % 7 == 0 and i % 5 == 0):
        print(i, end=" ")

