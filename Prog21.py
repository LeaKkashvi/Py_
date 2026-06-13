def areaS():
    s=float(input("Enter length of square: "))
    return s**2
def areaR():
    l=float(input("Enter length of rectangle: "))
    b=float(input("Enter breadth of rectangle: "))
    return l*b
def areaC():
    r=float(input("Enter radius of circle: "))
    return 3.14*r**2
print("Area of square:", areaS())
print("Area of rectangle:",areaR())
print("Area of circle:",areaC())
