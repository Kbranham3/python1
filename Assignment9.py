def check_character():
    user_input = input("Enter a single letter: ").strip()

    # Ensure the input is a single character and a letter
    if len(user_input) != 1 or not user_input.isalpha():
        print("Invalid input! Please enter only a single letter.")
        return

    # Convert to lowercase for easy comparison
    char = user_input.lower()

    # Check if the character is a vowel or consonant
    if char in "aeiou":
        print(f"'{user_input}' is a vowel.")
    else:
        print(f"'{user_input}' is a consonant.")

# Run the function
check_character()
