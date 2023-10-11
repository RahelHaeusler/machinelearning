# Simple String exercise

def main():
    number_string = input("Enter a sequence of digits: ")

    # Call the function
    total = string_total(number_string)

    # print the result
    print(f'The total of digits is {total}')


def string_total(string):
    number = 0
    total = 0

    for i in range(len(string)):
        # Converter char to integer
        number = int(string[i])

        # Accumulation
        total += number

        return total


if __name__ == '__main__':
    main()
