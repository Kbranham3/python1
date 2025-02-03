def classify_age():
    while True:
        try:
            age = int(input("Enter your age: ").strip())

            if age <= 0:
                print("Invalid input! Please enter a positive integer.")
                continue

            # Classify the age category
            if age < 18:
                category = "Minor"
            elif 18 <= age <= 65:
                category = "Adult"
            else:
                category = "Senior Citizen"

            print(f"Age {age}: You are classified as a {category}.")
            break  # Exit loop after a valid input
        except ValueError:
            print("Invalid input! Please enter a valid positive integer.")

# Run the function
classify_age()

