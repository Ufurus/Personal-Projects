# This program will help count words in a text

print("Enter text below, and it will print how many letters does it contain!")
entered_text = input("Enter text: ")

counter = 0
word_counter = 0

if len(entered_text) == 0:

    print("No words provided!")

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