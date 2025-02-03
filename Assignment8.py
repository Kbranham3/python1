def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: Marks must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")

# Get valid marks for three subjects
subjects = ["Math", "Science", "English"]
marks = [get_valid_mark(subject) for subject in subjects]

# Calculate average
average = sum(marks) / len(marks)

# Determine grade
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Display result
grade = get_grade(average)
print(f"Your average mark is: {average:.2f}")
print(f"Your grade is: {grade}")


