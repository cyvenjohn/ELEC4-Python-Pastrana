# Full Name: Cyven John J. Pastrana
# Section: IV-BSIT A
# Activity: Safe Menu Program
# Date: November 23, 2026

while True:
    print("\nSAFE MENU")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("3. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2

        except ValueError:
            print("Invalid input. Enter numbers only.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")

        else:
            print("Result:", result)

        finally:
            print("Division attempt finished.")

    elif choice == "2":
        try:
            filename = input("Enter file name: ")

            with open(filename, "r", encoding="utf-8") as file:
                contents = file.read()

        except FileNotFoundError:
            print("File not found.")

        except OSError:
            print("Cannot open this file.")

        except UnicodeError:
            print("Please open a UTF-8 text file.")

        except ValueError:
            print("Invalid file name.")

        else:
            print("File contents:")
            print(contents)

        finally:
            print("File reading attempt finished.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter 1, 2, or 3.")