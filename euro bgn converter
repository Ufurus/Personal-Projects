# asking for currency
chosen_first_currency = input("choose currency to convert from: ")
chosen_second_currency = input("choose currency to convert to: ")

while True:

    money_amount = float(input(f"Enter how much {chosen_first_currency} you want to convert: ")) # asking for money
    # amount or how much money

    if chosen_first_currency != "euro" or chosen_second_currency != "bgn": # catching if another currency is entered.

        print("Unsupported currency at the moment!")
        break

    if chosen_first_currency == "bgn": # lev to euro converter formula

        if chosen_second_currency == "euro":
            calculated_sum = money_amount * 0.51
            print(f"{calculated_sum:.2f } {chosen_first_currency}")
            break

    elif chosen_first_currency == "euro": # euro to lev converter formula

        if chosen_second_currency == "bgn":
            calculated_sum = money_amount / 1.96
            print(f"{calculated_sum:.2f} {chosen_second_currency}")
            break
