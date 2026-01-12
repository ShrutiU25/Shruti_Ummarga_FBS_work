#3. Create a class MedicalStudent inherited from Student with following:
#i. Data members :Specialization
#ii. MarksOfInternship
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

class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, internship_marks):
        super().__init__(student_id, name, age, percentage)
        self.specialization = specialization
        self.internship_marks = internship_marks

    def accept(self):
        super().accept()
        self.specialization = input("Enter Specialization: ")
        self.internship_marks = float(input("Enter Internship Marks: "))

    def display(self):
        super().display()
        print("Specialization:", self.specialization)
        print("Internship Marks:", self.internship_marks)

    # Overriding calculateRank
    def calculateRank(self):
        final_score = (self.percentage * 0.6) + (self.internship_marks * 0.4)

        if final_score >= 85:
            return "Excellent"
        elif final_score >= 70:
            return "Very Good"
        elif final_score >= 50:
            return "Good"
        else:
            return "Fail"

    def __str__(self):
        return (f"MedicalStudent[ID={self.student_id}, Name={self.name}, "
                f"Specialization={self.specialization}, "
                f"Percentage={self.percentage}, "
                f"InternshipMarks={self.internship_marks}, "
                f"Result={self.calculateRank()}]")

m1 = MedicalStudent(0, "", 0, 0.0, "", 0.0)

m1.accept()
m1.display()

print("Result:", m1.calculateRank())
print(m1)
