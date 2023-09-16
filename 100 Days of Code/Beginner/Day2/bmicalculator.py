weight = int(input("What is your weight in kg?: "))
height = float(input("What is your height in meters?: "))

bmi = str(round(weight / height ** 2))

print("Your BMI is " + bmi)