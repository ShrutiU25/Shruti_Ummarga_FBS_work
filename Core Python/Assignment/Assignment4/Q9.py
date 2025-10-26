#9. WAP to print all numbers in a range divisible by a given number.

start_num = int(input("Enter start of range: "))
end_num = int(input("Enter end of range: "))
div = int(input("Enter the divisor: "))

print(f"Numbers divisible by {div} in range:")

for i in range(start_num, end_num+1):
    if(i % div == 0):
        print(i, end=" ")

