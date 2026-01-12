#4. Create a class College which has collection of students. Add the following methods :
#a. Parameteried constructor for number of students.
#b. AddStudent
#c. GetStudent
#d. RemoveStudent
#e. Override __str__ Method

class College:
    def __init__(self, no_of_students):
        self.no_of_students = no_of_students
        self.students = []

    def addStudent(self, student_name):
        if len(self.students) < self.no_of_students:
            self.students.append(student_name)
            print(f"{student_name} added successfully.")
        else:
            print("Student limit reached!")

    def getStudent(self, student_name):
        if student_name in self.students:
            print(f"{student_name} is present in college.")
            return student_name
        else:
            print(f"{student_name} not found.")
            return None

    def removeStudent(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} removed successfully.")
        else:
            print(f"{student_name} not found.")

    def __str__(self):
        return f"College Students ({len(self.students)}/{self.no_of_students}): {self.students}"

college = College(3)

college.addStudent("Shruti")
college.addStudent("Amit")
college.addStudent("Neha")

college.getStudent("Amit")
college.removeStudent("Neha")

print(college)
