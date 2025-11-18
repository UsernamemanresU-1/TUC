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

        if choice == "7":
            print("Exiting...")
            break
        else:
            print("This option is not implemented yet.")


if __name__ == "__main__":
    main()
