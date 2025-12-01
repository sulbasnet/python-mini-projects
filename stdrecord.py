def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")

    with open("students.txt", "a") as file:
        file.write(f"{name}, {age}, {grade}\n")
    print("Student added successfully!\n")

def view_students():
    try:
        with open("students.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No records found.\n")
            else:
                print("\nAll Students:")
                print(content)
    except FileNotFoundError:
        print("No record file found yet.\n")

def search_student():
    name = input("Enter student name to search: ").lower()
    found = False
    try:
        with open("students.txt", "r") as file:
            for line in file:
                if name in line.lower():
                    print("Found:", line.strip())
                    found = True
        if not found:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No record file found yet.\n")

while True:
    print("========== STUDENT RECORD MANAGER ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")
