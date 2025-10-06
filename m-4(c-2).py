from math import pi

print("Geometry calculator:")
print("1. Calculate rectangle area")
print("2. Calculate circle area")
options = int(input("Enter your choice (1 or 2): "))

def calculate_rectangle_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    result_1 = length * width 
    return result_1

def calculate_circle_area():
    radius = float(input("Enter radius: "))
    result_2 = pi * (radius ** 2)
    result_2_formated = f'{result_2:.2f}'
    return result_2_formated

if options == 1:
    r = calculate_rectangle_area()
    print(f"The area of rectangle is: {r}")
elif options == 2:
    r = calculate_circle_area()
    print(f"The area of circle is: {r}")
else:
    print("Invalid choice")