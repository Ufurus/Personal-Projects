def make_a_list(number):
    """This function returns and appends
    a list with a chosen number and length depends on the number itself"""
    number = int(number)

    for num in range(number):
        number_list.append(number)

number_list = []

chosen_number = input("Choose a number to make a list: ")
made_list = make_a_list(chosen_number)

print(number_list)