def get_non_negative_input(prompt):
    """
    Prompt the user for a non-negative numeric value.
    Continues prompting until a valid non-negative number is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input. Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

# Prompt the user for the time duration in hours with error handling
hours = get_non_negative_input("Enter the time duration in hours: ")

# Convert the time duration to minutes and seconds
minutes = hours * 60
seconds = hours * 3600

# Display the converted time duration
print(f"\n{hours} hour(s) is equivalent to:")
print(f"- {minutes:.2f} minute(s)")
print(f"- {seconds:.2f} second(s)")