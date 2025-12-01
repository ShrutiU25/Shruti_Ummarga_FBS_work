#Q11. Write a program to print all numbers which are divisible by m and n in the list.

def divisible(li, m, n):
    for i in li:
        if(i % m == 0 and i % n == 0):
            print(i)

li = [10, 12, 18, 20, 24, 30, 36]

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))
print(f"Numbers divisible by {m} and {n} are: ")

divisible(li, m, n)
