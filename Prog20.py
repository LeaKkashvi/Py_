# Smart Traffic Signal System – Set green signal duration based on vehicle count

vc=int(input("Enter the number of vehicles waiting at the traffic signal: "))
if vc <= 5:
    duration = 30
elif vc <= 10:
    duration = 60
elif vc <= 20:
    duration = 90
else:
    duration = 120
print("The green signal duration is:", duration, "seconds")
