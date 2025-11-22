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

        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
