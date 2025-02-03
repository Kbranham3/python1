++import math

def get_numeric_input(prompt):
    """
    Continuously prompt the user for input until a valid numeric value is provided.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Prompt the user for the coordinates of the first point
print("Enter coordinates for Point 1:")
x1 = get_numeric_input("x1: ")
y1 = get_numeric_input("y1: ")

# Prompt the user for the coordinates of the second point
print("\nEnter coordinates for Point 2:")
x2 = get_numeric_input("x2: ")
y2 = get_numeric_input("y2: ")

# Calculate the distance between the two points using the distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the calculated distance
print(f"\nThe distance between the two points is: {distance:.2f}")
