# Full Name: Cyven John J. Pastrana
# Section: IV-BSIT A
# Activity: Student Record Manager
# Date: November 23, 2026

students = []
student_set = set()


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be blank.")

    elif name.lower() in student_set:
        print("Student already exists!")

    else:
        students.append(name)
        student_set.add(name.lower())
        print("Student added successfully!")


def remove_student():
    name = input("Enter full student name to remove: ").strip()

    if name == "":
        print("Name cannot be blank.")
        return

    for student in students:
        if name.lower() == student.lower():
            students.remove(student)
            student_set.remove(student.lower())
            print("Student removed successfully!")
            return

    print("Student not found!")


def search_student():
    search = input("Enter full or partial name: ").strip()

    if search == "":
        print("Search cannot be blank.")
        return

    count = 0
    print("\nSEARCH RESULTS")

    for student in students:
        if search.lower() in student.lower():
            count += 1
            print(f"{count}. {student}")

    if count == 0:
        print("Student not found!")

    print("Total matches:", count)


def display_students():
    print("\nSTUDENT LIST")

    # Sort nya yung names alphabetically, ignoring capital letters.
    students.sort(key=str.lower)

    number = 1

    for student in students:
        print(f"{number}. {student}")
        number += 1

    if len(students) == 0:
        print("No students added yet.")

    print("Total students:", len(students))


def main():
    
    while True:
        print("\nSTUDENT RECORD MANAGER")
        print("1. Add student")
        print("2. Remove student")
        print("3. Search student")
        print("4. Display all students")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Enter 1 to 5.")


if __name__ == "__main__":
    main()


# A list keeps items in order and allows duplicates.
# A set stores unique items and does not guarantee their order.
# I used the students list to store and display the original names.
# I used student_set to store lowercase names for duplicate checking.
# When removing a student, I remove the name from both collections.