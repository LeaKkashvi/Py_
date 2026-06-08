#Cab Fare Calculator – Calculate fare using distance slabs

d= float(input("Enter distance traveled in km: "))
if d <= 5:
    fare = d * 10
elif d <= 15:
    fare = 5 * 10 + (d - 5) * 8
elif d <= 30:
    fare = 5 * 10 + 10 * 8 + (d - 15) * 6
else:
    fare = 5 * 10 + 10 * 8 + 15 * 6 + (d - 30) * 5
print("The cab fare is:", fare)
