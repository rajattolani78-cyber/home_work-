import math

a_1 = int(input("enter the coefficient of x^2: "))
a_2 = int(input("enter the coefficient of x: "))
a_3 = int(input("enter the constant term: "))

# Correct discriminant
D = a_2**2 - 4*a_1*a_3

if D > 0:
    root_1 = (-a_2 + math.sqrt(D)) / (2 * a_1)
    root_2 = (-a_2 - math.sqrt(D)) / (2 * a_1)
    print(f"Two real roots: {root_1} and {root_2}")

elif D == 0:
    root_n = -a_2 / (2 * a_1)
    print(f"One real root: {root_n}")

else:
    real_part = -a_2 / (2 * a_1)
    imag_part = math.sqrt(-D) / (2 * a_1)
    print(f"Complex roots: {real_part} + {imag_part}i and {real_part} - {imag_part}i")