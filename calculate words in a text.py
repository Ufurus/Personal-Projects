# This program will help count words in a text

print("Enter text below, and it will print how many letters does it contain!")
entered_text = input("Enter text: ")

counter = 0
word_counter = 0

if len(entered_text) == 0: # check if no words are provided

    print("No words provided!")

# Below checks if string is more than 0 in terms of length, but whitespaces are also considered as length.
# As so, if perhaps the space-bar was hit several times it will add those whitespaces to the string, thus making it
# 0 < which we need to check if this length is whitespace or not.

if len(entered_text) > 0:

    if entered_text.isspace():

        print("No words provided!")

    else:

        for letter in entered_text:

            if letter.isalpha():

                counter += 1

            if letter.isspace():

                word_counter += 1

        if counter > 0:

            word_counter += 1

        print(f"Total word count: {word_counter}")