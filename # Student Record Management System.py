# Student Record Management System

students = {}          # to store student records
student_ids = {0}    # to avoid duplicate IDs
#student_ids = set()
courses = ("CSE", "CSD", "ML", "AI", "MCA", "ECE")

def add_student():
    sid = input("Enter Student ID: ")

    if sid in student_ids:
        print(" Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input(f"Enter course {courses}: ")
    marks = float(input("Enter Marks: "))

    student_data = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks
    }

    students[sid] = student_data
    student_ids.add(sid)
    print(" Student added successfully!")


def view_student():
    if not students:
        print("No records found!")
        return

    print("\n------ All Student Records ------")
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}, Marks: {info['Marks']}")


def search_student():
    sid = input("Enter Student ID to search: ")

    if sid in students:
        info = students[sid]
        print("\nStudent Found:")
        print(f"Name: {info['Name']}")
        print(f"Age: {info['Age']}")
        print(f"Course: {info['Course']}")
        print(f"Marks: {info['Marks']}")
    else:
        print(" Student not found!")


def del_student():
    sid = input("Enter Student ID to delete: ")

    if sid in students:
        del students[sid]
        student_ids.remove(sid)
        print(" Student deleted successfully!")
    else:
        print(" Student not found!")


# --------- MENU LOOP ---------

while True:
    print("\n=========== Student Record Management System =============")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        del_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")