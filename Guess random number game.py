from random import randint

print("Welcome! Numbers will be generated from 1 to 100, you have to guess which is the chosen number!")
print("Depending on the number, hints will be dropped, if you are below the number it will give a hint")
print("And for being above the number, it will give the same and vice versa.")
random_number = randint(0, 100)

while True:

    chosen_number = int(input("Enter the chosen number: "))

    if chosen_number == random_number:
        print("You guessed it!")
        print(f"The number was {chosen_number}")
        break

    if chosen_number < random_number:
        print("Below!")
        print("Go higher")

    elif chosen_number > random_number:
        print("Higher!")
        print("Go lower")