target_number = input('Enter number to convert to roman number: ') # first target num = 55

                   #0  #1   #2  #3  #4  #5  #6
number_position = ['I','V','X','L','C','D','M'] # I - last one, M - first one rule, used to determine position
roman_numbers = ['I','V','X','L','C','D','M'] # used to display the actual numbers

symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

if target_number.startswith('0'):
    print('Wrong number entered')
    exit()

if len(target_number) > 1:
    pass

else:
    if int(target_number) < 4:
        target_number = number_position[0] * int(target_number)
        print(target_number)
    elif int(target_number) >= 4:
        for key, value in symbols.items():
            if int(target_number) == value:
