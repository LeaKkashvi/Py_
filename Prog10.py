# BMI Category Finder- BMI and display category

h= float(input("Enter height in meters: "))
w= float(input("Enter weight in kilograms: "))
bmi= w/(h**2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
else:
    print("Overweight")