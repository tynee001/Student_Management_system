import os

FILENAME = "student.txt"

def load_students():
    """Helper function to load all students from the file."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip().split(",") for line in file if line.strip()]

def save_students(students):
    """Helper function to save the updated student list back to the file."""
    with open(FILENAME, "w") as file:
        for student in students:
            file.write(",".join(student) + "\n")

def register_student():
    students = load_students()
    
    # Generate ID
    if not students:
        student_id = "STD-001"
    else:
        last_id = students[-1][0]
        number = int(last_id.split("-")[1]) + 1
        student_id = f"STD-{number:03d}"

    name = input("Enter student name: ")
    age = input("Enter student age: ")
    department = input("Enter student department: ")

    students.append([student_id, name, age, department])
    save_students(students)
    
    print(f"\nStudent registered successfully! ID: {student_id}")

def display_students():
    students = load_students()
    if not students:
        print("\nNo students registered.")
        return

    print("\n========== STUDENTS ==========")
    for s in students:
        print(f"ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | Dept: {s[3]}")
        print("-" * 30)

def search_student():
    search_id = input("Enter student ID to search: ")
    students = load_students()
    
    for s in students:
        if s[0] == search_id:
            print(f"\nFound! ID: {s[0]} | Name: {s[1]} | Age: {s[2]} | Dept: {s[3]}")
            return
            
    print("\nStudent not found.")

def update_student():
    search_id = input("Enter student ID to update: ")
    students = load_students()
    updated = False

    for s in students:
        if s[0] == search_id:
            print(f"Current Info -> Name: {s[1]}, Age: {s[2]}, Dept: {s[3]}")
            s[1] = input("Enter new name (leave blank to keep): ") or s[1]
            s[2] = input("Enter new age (leave blank to keep): ") or s[2]
            s[3] = input("Enter new department (leave blank to keep): ") or s[3]
            updated = True
            break

    if updated:
        save_students(students)
        print("\nStudent updated successfully!")
    else:
        print("\nStudent not found.")

def delete_student():
    search_id = input("Enter student ID to delete: ")
    students = load_students()
    
    # Filter out the student with the matching ID
    new_students = [s for s in students if s[0] != search_id]

    if len(new_students) < len(students):
        save_students(new_students)
        print("\nStudent deleted successfully!")
    else:
        print("\nStudent not found.")

def main():
    while True:
        print("\n==============================")
        print("      STUDENT RECORD SYSTEM")
        print("==============================")
        print("1. Register Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            register_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("\nThank you for using the system!")
            break
        else:
            print("\nInvalid choice. Please select between 1 and 6.")

if __name__ == "__main__":
    main()