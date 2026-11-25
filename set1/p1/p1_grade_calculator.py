# Full Name: Cyven John J. Pastrana
# Section: IV-BSIT A
# Activity: Student Grade Calculator
# Date: November 23, 2026

passingAverage = 75

def countGrades():

    while True:
        try:
            count = int(input("How many grades will you input? "))
            if count > 0:
                break
            print("---Please enter a whole number greater than 0---")
        except ValueError:
                print("---Enter a valid whole number.---")


    grades = []

    for number in range(1, count + 1):
          while True:
            try:
                grade = float(input(f"Enter grade {number}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("---Grade must be from 0 to 100.---")
            except ValueError:
                print("---Invalid input. Please enter a number.---")
    return grades


def calculateAverage(grades):
    return sum(grades) / len(grades)


def getHighest(grades):
    return max(grades)


def getLowest(grades):
    return min(grades)


def getStatus(grades):
    if calculateAverage(grades) >= passingAverage:
        return "Passed"
    return "Failed"

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

            print("\nGRADE RESULTS")
            print(f"Average: {calculateAverage(grades):.2f}")
            print(f"Highest: {getHighest(grades):.2f}")
            print(f"Lowest: {getLowest(grades):.2f}")
            print(f"Status: {getStatus(grades)}")

        elif choice == "3":
            print("Thank you. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()



# A local variable is defined inside a function and used within that function.
# For example, count is a local variable inside countGrades().
# The grades variable inside main() is passed as an argument to other functions.
# A global variable is defined outside functions and can be accessed inside them.
# In this program, passingAverage is a global variable read by getStatus().