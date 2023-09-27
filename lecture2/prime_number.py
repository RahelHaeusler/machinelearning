import sympy

# prim numbers are only applicable for int
number = int(input("Please enter a integer: "))

if sympy.isprime(number):
    print(number, "is prime")
else:
    print(number, "is not prime")
