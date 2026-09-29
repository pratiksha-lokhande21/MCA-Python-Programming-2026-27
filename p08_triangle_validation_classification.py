side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:

    print("Valid Triangle")

    if side1 == side2 and side2 == side3:
        print("Equilateral Triangle")

    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Invalid Triangle")