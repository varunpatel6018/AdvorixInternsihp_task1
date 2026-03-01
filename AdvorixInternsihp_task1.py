import csv
import os

FILE_NAME = "students.csv"


# ------------------ FILE INITIALIZE ------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course", "Semester", "Marks"])


# ------------------ ADD STUDENT ------------------
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    semester = input("Enter Semester: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([sid, name, age, course, semester, marks])

    print("✅ Student added successfully!\n")


# ------------------ VIEW STUDENTS ------------------


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) == 1:
                print("⚠ No records found\n")
                return

            print("\n------ STUDENT RECORDS ------")
            for row in data:
                print("{:<10} {:<15} {:<5} {:<10} {:<10} {:<5}".format(*row))
            print()

    except:
        print("❌ File not found\n")


# ------------------ UPDATE STUDENT ------------------
def update_student():
    sid = input("Enter Student ID to update: ")
    updated = False
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == sid:
                print("Enter new details:")
                row[1] = input("New Name: ")
                row[2] = input("New Age: ")
                row[3] = input("New Course: ")
                row[4] = input("New Semester: ")
                row[5] = input("New Marks: ")
                updated = True
            rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if updated:
        print("✅ Student updated successfully!\n")
    else:
        print("❌ Student ID not found\n")


# ------------------ DELETE STUDENT ------------------
def delete_student():
    sid = input("Enter Student ID to delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != sid:
                rows.append(row)
            else:
                deleted = True

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if deleted:
        print("🗑 Student deleted successfully!\n")
    else:
        print("❌ Student ID not found\n")


# ------------------ MENU ------------------



def menu():
    initialize_file()

    while True:
        print("====== STUDENT MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("⚠ Invalid choice\n")


# ------------------ RUN ------------------


menu()