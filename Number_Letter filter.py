def numbers(number_list):
    return numbers_list

def letters(letter_list):
    return letters_list

entered_elements = input("Enter a list of elements: ").split(", ")

numbers_list = []
letters_list = []

for element in entered_elements:

    if element.isalpha():
        letters_list.append(element)

    if element.isdigit():
        numbers_list.append(element)


chosen_list = input("Which list do you want to see? [Numbers] or [Letters] or both?: ").lower()

if chosen_list == "numbers":
    action = numbers(numbers_list)
    print(action)

elif chosen_list == "letters":
    action = numbers(letters_list)
    print(action)

elif chosen_list == "both":
    first_action = numbers(numbers_list)
    second_action = letters(letters_list)
    print(f"Numbers: {first_action}")
    print(f"Letters: {second_action}")