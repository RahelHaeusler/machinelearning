
# Exercise 5 Chapter 9

def main():
    input_file = open("text.txt", "r")
    text = input_file.read()
    all_punct = ",.-?!"

    # Running through the loop and removing all punctuation
    for element in text:
        if element in all_punct:
            text = text.replace(element, "")

    words = text.split(" ")
    # store result in the same list after transforming everything in lower case
    words = [word.lower() for word in words]

    # create set with
    unique_words = set(words)
    unique_words = sorted(unique_words)

    # print all the words
    for word in unique_words:
        print(word)

    input_file.close()


# Call the main function.
if __name__ == '__main__':
    main()