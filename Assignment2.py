def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_area(length, width):
    return length * width
# Get valid inputs
length = get_positive_number("Enter the length of the rectangle: ")
width = get_positive_number("Enter the width of the rectangle: ")

# Calculate area
area = calculate_area(length, width)

# Display result
print(f"The area of the rectangle is: {area:.2f}")