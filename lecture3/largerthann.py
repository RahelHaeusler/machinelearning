# Main function
def main():
    my_list = [1, 2, 3, 4, 5, 6, 15]
    threshold = 4
    print_values(threshold, my_list)


# Printing the values larger than the threshold
def print_values(threshold, my_list):
    for val in my_list:
        if val > threshold:
            print(val)


# Calling the main function
if __name__ == '__main__':
    main()
