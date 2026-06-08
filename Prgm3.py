#Electricity Bill Calculator

units = float(input("Enter the number of units consumed: "))
if units <= 100:
    bill = units * 0.5
elif units <= 200:
    bill = 100 * 0.5 + (units - 100) * 0.75

elif units <= 300:
    bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
else:
    bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
print("The electricity bill is:", bill)

