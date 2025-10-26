#2.Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. 
#Display all percentage and average percentage of students.

n = int(input("Enter number of students: "))

total_percent = 0 

for i in range(1, n + 1):
    print(f"\nEnter marks of 5 subjects for student {i}:")
    s1 = float(input("Subject 1: "))
    s2 = float(input("Subject 2: "))
    s3 = float(input("Subject 3: "))
    s4 = float(input("Subject 4: "))
    s5 = float(input("Subject 5: "))

    total = s1 + s2 + s3 + s4 + s5
    percent = (total / 500) * 100

    print(f"Percentage of student {i}: {percent:.2f}%")

    total_percent += percent 

avg_percent = total_percent / n
print(f"\nAverage percentage of all students: {avg_percent:.2f}%")
