#2. WAP a menu driven program to perform following operations using files :
#a. Add a record
#b. Search for a record using id
#c. Delete a record using id
#d. Edit a record using id.
#e. Display all records.

import pickle
import os

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(self.eid, self.ename, self.basic)


# ---------- Add Record ----------
def add_record():
    f = open("emp.dat", "ab")
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    emp = Emp(eid, ename, basic)
    pickle.dump(emp, f)
    f.close()
    print("Record added successfully")


# ---------- Search Record ----------
def search_record():
    eid = int(input("Enter Employee ID to search: "))
    found = False
    try:
        f = open("emp.dat", "rb")
        while True:
            emp = pickle.load(f)
            if emp.eid == eid:
                print("Record Found:")
                emp.display()
                found = True
                break
        f.close()
    except EOFError:
        f.close()
    if not found:
        print("Record not found")


# ---------- Delete Record ----------
def delete_record():
    eid = int(input("Enter Employee ID to delete: "))
    found = False
    f1 = open("emp.dat", "rb")
    f2 = open("temp.dat", "wb")

    try:
        while True:
            emp = pickle.load(f1)
            if emp.eid != eid:
                pickle.dump(emp, f2)
            else:
                found = True
    except EOFError:
        pass

    f1.close()
    f2.close()

    os.remove("emp.dat")
    os.rename("temp.dat", "emp.dat")

    if found:
        print("Record deleted successfully")
    else:
        print("Record not found")


# ---------- Edit Record ----------
def edit_record():
    eid = int(input("Enter Employee ID to edit: "))
    found = False
    f1 = open("emp.dat", "rb")
    f2 = open("temp.dat", "wb")

    try:
        while True:
            emp = pickle.load(f1)
            if emp.eid == eid:
                print("Enter new details")
                ename = input("Enter New Name: ")
                basic = float(input("Enter New Basic Salary: "))
                emp = Emp(eid, ename, basic)
                found = True
            pickle.dump(emp, f2)
    except EOFError:
        pass

    f1.close()
    f2.close()

    os.remove("emp.dat")
    os.rename("temp.dat", "emp.dat")

    if found:
        print("Record updated successfully")
    else:
        print("Record not found")


# ---------- Display Records ----------
def display_records():
    try:
        f = open("emp.dat", "rb")
        print("ID   Name   Salary")
        while True:
            emp = pickle.load(f)
            emp.display()
        f.close()
    except EOFError:
        f.close()


# ---------- Main Menu ----------
while True:
    print("\n1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_record()
    elif ch == 2:
        search_record()
    elif ch == 3:
        delete_record()
    elif ch == 4:
        edit_record()
    elif ch == 5:
        display_records()
    elif ch == 6:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
