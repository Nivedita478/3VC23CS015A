# Student Attendance Management System

students = {}

def add_student():
    name = input("Enter student name: ")
    students[name] = []
    print("Student added successfully!")

def mark_attendance():
    name = input("Enter student name: ")
    
    if name in students:
        status = input("Enter Present/Absent: ")
        students[name].append(status)
        print("Attendance marked!")
    else:
        print("Student not found")

def view_attendance():
    for name, records in students.items():
        print(name, ":", records)

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        mark_attendance()
    elif choice == 3:
        view_attendance()
    elif choice == 4:
        break
    else:
        print("Invalid choice")