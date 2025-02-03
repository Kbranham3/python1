# Prompt the user to enter weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI using the formula: BMI = Weight / (Height^2)
bmi = weight / (height ** 2)

# Display the calculated BMI
print(f"Your BMI is: {bmi:.2f}")

# Provide feedback based on the BMI category
if bmi < 18.5:
    print("You are underweight. It may be beneficial to consult with a healthcare provider or nutritionist for advice on gaining weight in a healthy way.")
elif 18.5 <= bmi < 25:
    print("You are at a normal weight. Great job maintaining a healthy lifestyle!")
elif 25 <= bmi < 30:
    print("You are overweight. Consider reviewing your diet and exercise habits to help achieve a healthier weight.")
else:  # bmi >= 30
    print("You are obese. It is advisable to consult with a healthcare provider for personalized guidance and support.")
