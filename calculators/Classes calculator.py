class Numbers:

    def __init__(self, first_number: int, second_number: int):
        self.first_number = first_number
        self.second_number = second_number

    def multiply(self):
        return self.first_number * self.second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def division(self):
        return self.first_number / self.second_number

while True:

    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    selected_action = input("Please, select an action to perform:\nadd ; sub ; multi ; div; end:  ")
    calculate = Numbers(first_num, second_num)

    if selected_action.lower() == "end":
        print("Thank you for calculating!")
        break
    else:

        if selected_action.lower() == "add":
            print(f"{first_num} + {second_num} = {calculate.addition()}")
        elif selected_action.lower() == "sub":
            print(f"{first_num} - {second_num} = {calculate.subtract()}")
        elif selected_action.lower() == "multi":
            print(f"{first_num} * {second_num} = {calculate.multiply()}")
        elif selected_action.lower() == "div":
            print(f"{first_num} / {second_num} = {calculate.division()}")
        else:
            print("No such action! Thank you for calculating.")
            break