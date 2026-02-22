def decimal_to_binary(given_number):
    final_result = ''
    while given_number > 0: # 35
        final_result += str(given_number % 2)
        given_number //= 2
    return final_result

def binary_to_decimal(given_number):
    final_result = []
    power = len(given_number) - 1
    for num in given_number:
        final_result.append(num*2**power)
        power -= 1
    return sum(final_result)

print("*" * 5, "Please enter number to convert to decimal/binary", "*" * 5)
print("If you want to end the program, enter 'end' to exit the program")

while True:

    chosen_number = input("Please enter a number: ")
    if chosen_number == "end":
        print("Thanks for using this program!")
        break
    try:
        chosen_number = int(chosen_number)
    except ValueError:
            print("Please enter a valid number")
            continue
    chosen_system = input("Please enter your system(decimal/binary): ")

    if chosen_system == "decimal":
        chosen_number = [int(x) for x in str(chosen_number)]
        final_number = binary_to_decimal(chosen_number)
        print(f"{''.join(str(x) for x in chosen_number)} in decimal is {final_number}")
    elif chosen_system == "binary":
        final_number = decimal_to_binary(chosen_number)
        print(f"{chosen_number} in binary is {final_number}")
