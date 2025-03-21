def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"

def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"{subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def generate_report_card(students):
    print("\nReport Cards:")
    for student in students:
        print(f"\nName: {student['name']}, Roll Number: {student['roll']}")
        print(f"Math: {student['math']}, Physics: {student['physics']}, Urdu: {student['urdu']}, English: {student['english']}, Computer: {student['computer']}")
        total = sum(student[subject] for subject in ['math', 'physics', 'urdu', 'english', 'computer'])
        percentage = total / 5
        grade = calculate_grade(percentage)
        print(f"Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")

def main():
    students = []
    while True:
        print("\nEnter student details:")
        try:
            name = input("Student Name: ")
            roll = input("Roll Number: ")
            math = get_valid_marks("Math")
            physics = get_valid_marks("Physics")
            urdu = get_valid_marks("Urdu")
            english = get_valid_marks("English")
            computer = get_valid_marks("Computer")
        except ValueError:
            print("Invalid input! Please enter valid data.")
            continue

        student = {
            "name": name,
            "roll": roll,
            "math": math,
            "physics": physics,
            "urdu": urdu,
            "english": english,
            "computer": computer
        }
        students.append(student)
        print(f"Record of {name} inserted successfully.")
        
        more = input("Do you want to insert more? Press 'Y' for Yes or 'N' for No: ").strip().lower()
        if more == 'n':
            break
        elif more != 'y':
            print("Invalid choice! Ending input phase.")
            break

    generate_report_card(students)

if __name__ == "__main__":
    main()

