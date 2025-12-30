def calculate_bmi(weight, height):
    return weight / (height * height)

print("BMI CALCULATOR")

try:
    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))
    height = height_cm / 100

    if weight <= 0 or height <= 0:
        print("Please enter valid positive numbers.")
    else:
        bmi = calculate_bmi(weight, height)
        print("Your BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Invalid input. Please enter numbers only.")
