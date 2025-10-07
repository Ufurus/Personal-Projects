number_list = ["3", "4", "72", "100", "23", "45", "72", "6"]
guesses = 0

print(number_list)
print("From the list above, choose a number and if guess correctly - you win!")
print("You have three guesses. Use them wisely ;)")

while True:

    chosen_number = input("Choose a number: ")

    if chosen_number == "6":
        print("You guessed it right!")
        break

    else:
        guesses += 1
        print("wrong guess!")

    if guesses > 3:
        print("Out of available guesses\nyou loose!")
        break