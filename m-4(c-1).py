def celsius_to_fahrenheit(t):
   Fahrenheit = (t * 9/5) + 32
   return Fahrenheit
r = celsius_to_fahrenheit(float(input("fahrenheit_to_celsius ")))
print(celsius_to_fahrenheit(r))

def fahrenheit_to_celsius(fahrenheit):
   Celsius = (fahrenheit - 32) * 5/9
   return Celsius
c = fahrenheit_to_celsius(float(input("fahrenheit_to_celsius ")))
print,fahrenheit_to_celsius(c)


