def calculator(chosen_action, a, b):

    if chosen_action == "*":
        return a * b

    elif chosen_action == "/":
        return a / b

    elif chosen_action == "+":
        return a + b

    elif chosen_action == "-":
        return a - b

    elif chosen_action == "%":
        return a % b

    else:
        print("Please choose appropriate action!")

print("[*] | [/] | [+] | [-] | [%]")
action = input("Please choose an action to perform: ")
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

result = calculator(action,first_num, second_num)

if result == None:
    pass

else:

    print(f"{first_num} {action} {second_num} = {result}")
