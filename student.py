
students = []

def add_student():
    name = input("Enter name: ")
    rollno = int(input("Enter Roll Number: "))
    marks = int(input("Enter Marks: "))

    student = {
        "Name": name,
        "Roll": rollno,
        "Marks": marks
    }

    students.append(student)
    print("Student added successfully")


def view_students():
    if len(students) == 0:
        print("No students found")
    else:
        for s in students:
            print(s)


def search_student():
    roll = int(input("Enter roll number to search: "))

    for s in students:
        if s["Roll"] == roll:
            print("Found:", s)
            return

    print("Student not found")


def delete_student():
    roll = int(input("Enter roll number to delete: "))

    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("Deleted successfully")
            return

    print("Student not found")


while True:
    print("\n--- Student Menu ---")
    print("1: Add student")
    print("2: View students")
    print("3: Search student")
    print("4: Delete student")
    print("5: Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        break
    elif choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    else:
        print("Invalid choice")