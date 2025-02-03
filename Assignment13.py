def check_palindrome():
    # Get user input for the string
    string = input("Enter a string: ").strip()

    # Convert the string to lowercase to ensure case-insensitive comparison
    string = string.lower()

    # Initialize two pointers: one at the start and one at the end
    left, right = 0, len(string) - 1

    # Loop to compare characters from both ends
    while left < right:
        if string[left] != string[right]:
            print("The string is not a palindrome.")
            return
        left += 1
        right -= 1

    print("The string is a palindrome.")

# Run the function
check_palindrome()
