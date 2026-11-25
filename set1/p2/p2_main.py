# Full Name: Cyven John J. Pastrana
# Section: IV-BSIT A
# Activity: Custom Module: student_utils
# Date: November 23, 2026

import student_utils
from student_utils import getStatus
from datetime import datetime


def countGrades():
    while True:
        try:
            count = int(input("How many grades will you input? "))

            if count > 0:
                break

            print("Please enter a whole number greater than 0.")
        except ValueError:
            print("Enter a valid whole number.")

    grades = []

    for number in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {number}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be from 0 to 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


def main():

    grades = []  

    while True:
        print("\nSTUDENT GRADE CALCULATOR")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            grades = countGrades()
            print("Grades saved successfully!")

        elif choice == "2":
            if not grades:
                print("---Please enter grades first.---")
                continue

            print("\nGRADE REPORT")
            print(f"Date and Time: {datetime.now():%Y-%m-%d %H:%M:%S}")
            print(f"Average: {student_utils.calculateAverage(grades):.2f}")
            print(f"Highest: {student_utils.getHighest(grades):.2f}")
            print(f"Lowest: {student_utils.getLowest(grades):.2f}")
            print(f"Status: {getStatus(grades)}")
                

        elif choice == "3":
            print("Thank you. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()