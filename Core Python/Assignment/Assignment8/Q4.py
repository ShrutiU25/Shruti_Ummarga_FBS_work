#4. Sum of all odd numbers between 1 to n

def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total

n = int(input("Enter value of n: "))
print(f"Sum of all odd numbers between 1 and {n} = {sum_of_odds(n)}")
