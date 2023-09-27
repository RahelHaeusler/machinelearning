# Calculation of some numbers

number = 1.0
total = 0.0

while number > 0:
    number = float(input("Enter a positive number: "))
    if number > 0:
        total += number
        print(f"Total = {total:.2f}")

    else:
        print("The calculation has ended")
        print(f"The total is = {total:.2f}")

