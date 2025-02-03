def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Get valid inputs
principal = get_valid_input("Enter the principal amount: ")
rate = get_valid_input("Enter the interest rate (in percentage): ")
time = get_valid_input("Enter the time period (in years): ")

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Display result
print(f"The calculated simple interest is: {simple_interest:.2f}")

