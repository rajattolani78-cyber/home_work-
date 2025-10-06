b = int(input("enter your base value: "))
e = int(input("enter your exponent value: "))
def power (base,exponent):
    if exponent > 0 :
       r = pow(base,exponent)
       print (f"{base} to power of {exponent} is: {r}")
       return r
    elif exponent == 0:
        r = 1 
        print(f"{base} to power of {exponent} is: {r}")
        return r    
power(b,e)
