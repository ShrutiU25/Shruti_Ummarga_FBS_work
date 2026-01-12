#2. Create a derived class from Student as EnggStudent with :
#a. Data members as :
#i. Branch
#ii. InternalMarks
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.student_id = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)

    def calculateRank(self):
        if self.percentage >= 85:
            return "Rank A"
        elif self.percentage >= 70:
            return "Rank B"
        elif self.percentage >= 50:
            return "Rank C"
        else:
            return "Fail"

    def __str__(self):
        return f"Student[ID={self.student_id}, Name={self.name}, Percentage={self.percentage}]"

class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.branch = branch
        self.internal_marks = internal_marks

    def accept(self):
        super().accept()
        self.branch = input("Enter Branch: ")
        self.internal_marks = float(input("Enter Internal Marks: "))

    def display(self):
        super().display()
        print("Branch:", self.branch)
        print("Internal Marks:", self.internal_marks)

    # Overriding calculateRank method
    def calculateRank(self):
        final_score = (self.percentage * 0.7) + (self.internal_marks * 0.3)

        if final_score >= 85:
            return "Distinction"
        elif final_score >= 70:
            return "First Class"
        elif final_score >= 50:
            return "Second Class"
        else:
            return "Fail"

    def __str__(self):
        return (f"EnggStudent[ID={self.student_id}, Name={self.name}, "
                f"Branch={self.branch}, Percentage={self.percentage}, "
                f"InternalMarks={self.internal_marks}, "
                f"Result={self.calculateRank()}]")

e1 = EnggStudent(0, "", 0, 0.0, "", 0.0)

e1.accept()
e1.display()

print("Result:", e1.calculateRank())
print(e1)

    
    
    
        