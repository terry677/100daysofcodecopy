print("Welcome to the BMI calculator!!!")

height = input("Enter you height in (meters): \n")
weight = input("Enter your weight in (kilogram): \n")

BMI = float(weight) / float(height) ** 2
BMI = round(BMI)
if BMI < 18.5:
    print("Your BMI is :" + str(BMI) + " and your are Under Weight")
elif BMI < 25:
    print("Your BMI is :" + str(BMI) + " and your are Normal Weight")
elif BMI < 30:
    print(f"Your BMI is : {BMI} and you are Over Weight")
elif BMI < 35:
    print(f"Your BMI is : {BMI} and you are Obese")
else:
    print(f"Your BMI is : {BMI} and you are Clinically Obese")
