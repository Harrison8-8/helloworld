def main():
    print("Student Qualify Apps")
    while True:
        lastName = input("Enter your last name: ")
        if lastName.upper() == 'ZZZ':
            print("Exiting")
            break
        firstName = input("Enter your first name: ")

        try: 
            gpa = float(input("Enter gpa: "))
        except ValueError:
            print("Invalid input. GPA must be a number")
            continue

        if gpa >= 3.5:
            print(f"{firstName} {lastName} made the Deans list")
        elif gpa >= 3.25:
            print(f"{firstName} {lastName}has made the honor roll")
        else:
            print(f"{firstName} {lastName} didn not make a list")

if __name__ == "__main__":
    main()