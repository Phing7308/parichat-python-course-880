"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

weight = float(input"Weight:"))
heigth = float(input("Height:"))
bmi = weigth / height ** 2
print("You BMI :",bmi)
if bmi < 18.5:
    print("Underweight")

if bmi >=18.5 and bmi <= 24.9:
    print("Normal Weight")

if bmi >=25.0 and bmi <=29.9:
    print("Overweight")

if bmi >=30.0:
    print("Obese")
"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""