
# Main Method
def main():
    try:
        # Open file for reading
        infile = open('numbers.txt', 'r')

        for line in infile:
            # strip command deletes all the blank spaces before and after
            print(line.strip())

        infile.close()

    # what will happen if it's not an an IO error?
    # except IOError:
    #     print("IOError occurred")
    # better

    except Exception:
        print("An error occurred")

    finally:
        print("Bye...")

# Call the main method


if __name__ == '__main__':
    main()
