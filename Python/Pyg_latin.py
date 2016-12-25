print("Welcome to the Pig Latin Translator!")


def input_word():
    original = input("Enter a word: ")
    if len(original) > 0 and original.isalpha():
        print(original)
    else:
        print("You did not enter a word")
        print("Try again.")
        return input_word()


input_word()
