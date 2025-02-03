ef
collatz_sequence():
while True:
    try:
        # Ask the user for input
        num = int(input("Enter a positive integer: ").strip())

        # Ensure the number is positive
        if num <= 0:
            print("Please enter a positive integer.")
            continue

        # Generate the Collatz sequence
        sequence = []
        while num != 1:
            sequence.append(num)
            if num % 2 == 0:
                num //= 2  # If even, divide by 2
            else:
                num = num * 3 + 1  # If odd, multiply by 3 and add 1

        sequence.append(1)  # Add 1 at the end of the sequence
        print("Collatz sequence:", sequence)
        break  # Exit after generating the sequence
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")

# Run the function
collatz_sequence()