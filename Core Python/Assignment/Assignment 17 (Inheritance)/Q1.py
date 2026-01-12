#1. Create a class Student with following
#a. data members :
#i. StudentId
#ii. Name
#iii. Age
#iv. Percentage
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. Method CalculateRank
#v. Override __str__ Method

class Student:
    def __init__(self, student_id, name, age, percentage):
        # Parameterized constructor
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        # Accept details from user
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        # Display student details
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)

    def calculateRank(self):
        # Calculate rank based on percentage
        if self.percentage >= 85:
            return "Rank A"
        elif self.percentage >= 70:
            return "Rank B"
        elif self.percentage >= 50:
            return "Rank C"
        else:
            return "Fail"

    def __str__(self):
        # Override __str__ method
        return (f"Student[ID={self.student_id}, "
                f"Name={self.name}, "
                f"Age={self.age}, "
                f"Percentage={self.percentage}, "
                f"Rank={self.calculateRank()}]")

s1 = Student(0, "", 0, 0.0)

s1.accept()
s1.display()

print("Rank:", s1.calculateRank())
print(s1)
