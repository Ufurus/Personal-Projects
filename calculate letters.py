# This program will help count letters in a text

print("Enter text below, and it will print how many letters does it contain")
entered_text = input("Enter text: ")

counter = 0

for letter in entered_text:

    if letter.isalpha():

        counter += 1

    else:

        pass

print(f"Total letter count: {counter}")