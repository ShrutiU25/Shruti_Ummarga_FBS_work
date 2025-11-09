#Q3. Write a program to accept basic salary of n emp (n should be accepted from user).
#If basic salary is below 20000 then da = 10%, ta = 12% and hra = 15% otherwise da = 15%, ta = 18% and hra = 20%
#Based on this calculate the total salary of each emp and also total salary of all emp

def emp(n):
    sum_total = 0
    for i in range(1, n + 1):
        basic_salary = int(input(f"Enter basic salary of employee {i}: "))

        if basic_salary < 20000:
            da = 10 / 100 * basic_salary
            ta = 12 / 100 * basic_salary
            hra = 15 / 100 * basic_salary
        else:
            da = 15 / 100 * basic_salary
            ta = 18 / 100 * basic_salary
            hra = 20 / 100 * basic_salary

        total = basic_salary + da + ta + hra
        print(f"Total salary of employee {i} = {total:.2f}")

        sum_total += total

    print("\nTotal salary of all employees =", sum_total)

n = int(input("Enter number of employees: "))
emp(n)
