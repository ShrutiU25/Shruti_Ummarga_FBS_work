#1. Create a class Emp (eid,ename,basic)

import pickle

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"Employee ID   : {self.eid}")
        print(f"Employee Name : {self.ename}")
        print(f"Basic Salary  : {self.basic}")
        print("-" * 30)


# ---------- Pickling ----------
def save_employee(emp):
    with open("employee.dat", "ab") as f:
        pickle.dump(emp, f)
    print("Employee data saved successfully!\n")


# ---------- Unpickling ----------
def read_employees():
    print("\nEmployee Records:\n")
    try:
        with open("employee.dat", "rb") as f:
            while True:
                emp = pickle.load(f)
                emp.display()
    except EOFError:
        pass


# ---------- Main Program ----------
while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        eid = int(input("Enter Employee ID: "))
        ename = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        emp = Emp(eid, ename, basic)
        save_employee(emp)

    elif choice == 2:
        read_employees()

    elif choice == 3:
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.")
