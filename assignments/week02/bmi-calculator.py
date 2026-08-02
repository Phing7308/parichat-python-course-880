weight = float(input("Weight: "))
height = float(input("Height: "))

bmi = weight / (height ** 2)

print(f"Your BMI: {bmi:.1f}")

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weight")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")