print("Choose numbers you want to calculate!")

print()

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("Please choose an action you want to do!")

print()

print("add (+) | subtraction (-) | multiplication (*) | division (/) | modulus (%)")

chosen_action = input("Chosen action: ")

if chosen_action == "+" or chosen_action == "-" or chosen_action == "*" or chosen_action == "/" or chosen_action == "%":

    if chosen_action == "+":

        result = first_number + second_number
        print(f"Result: {result}")

    elif chosen_action == "-":

        result = first_number - second_number
        print(f"Result: {result}")

    elif chosen_action == "*":

        result = first_number * second_number
        print(f"Result: {result}")

    elif chosen_action == "/":

        result = first_number / second_number
        print(f"Result: {result:.2f}")

    elif chosen_action == "%":

        result = first_number % second_number
        print(f"Result: {result}")

else:

    print("Error")
    print("Not a valid action chosen!")