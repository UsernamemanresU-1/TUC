import json
import os


def add_student(students, name):
    if name in students:
        print(f"Student {name} already exists!")
    else:
        students[name] = []
        print(f"Added student {name}.")


def add_grade(students, name, grade):
    if name not in students:
        print(f"Error: student {name} does not exist!")
        return

    try:
        grade = float(grade)
    except ValueError:
        print("Grade must be a number!")
        return

    if grade < 0 or grade > 100:
        print("Grade must be between 0 and 100.")
        return

    students[name].append(grade)
    print(f"Added grade {grade} for {name}.")


def average(students, name):
    if name not in students:
        print(f"Error: student {name} does not exist!")
        return None

    if len(students[name]) == 0:
        print(f"{name} has no grades yet.")
        return None

    avg = sum(students[name]) / len(students[name])
    print(f"Average for {name}: {avg:.2f}")
    return avg


def save_to_file(students, filename):
    try:
        with open(filename, "w") as f:
            json.dump(students, f)
        print(f"Saved to {filename}.")
    except Exception as e:
        print("Error saving file:", e)


def load_from_file(filename):
    if not os.path.exists(filename):
        print("Error: file does not exist!")
        return {}

    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print(f"Loaded from {filename}.")
        return data
    except Exception as e:
        print("Error loading file:", e)
        return {}


def main():
    students = {}

    while True:
        print("\nWelcome to Grade Manager!")
        print("1. Add student")
        print("2. Add grade")
        print("3. Show average for student")
        print("4. Show all students")
        print("5. Save to file")
        print("6. Load from file")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            add_student(students, name)

        elif choice == "2":
            name = input("Enter name: ")
            grade = input("Enter grade: ")
            add_grade(students, name, grade)

        elif choice == "3":
            name = input("Enter name: ")
            average(students, name)

        elif choice == "4":
            if not students:
                print("No students yet.")
            else:
                print("Students:")
                for n, grades in students.items():
                    print(f"  {n}: {grades}")

        elif choice == "5":
            filename = input("Enter filename: ")
            save_to_file(students, filename)

        elif choice == "6":
            filename = input("Enter filename: ")
            students = load_from_file(filename)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
