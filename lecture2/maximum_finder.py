
# Method for finding the maximum of two numbers
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Main method
def main():
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Maximum of the two number is , {maximum(num1, num2)}")

# Calling the main method
main()
