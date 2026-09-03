print('Please enter what kind of number do you want to use? (Binary/Decimal)')

number_type = input('Enter number type(Binary/Decimal): ').lower()
# basic number type check
while number_type != 'binary' and number_type != 'decimal':
    print('Please enter valid number type(Binary/Decimal)!')
    number_type = input('Enter number type(Binary/Decimal): ')
# basic check to see if number is actually number
given_number = input('Enter the given number: ')
while given_number.isdigit() != True:
    print('Please enter valid number!')
    given_number = input('Enter the given number: ')

if number_type == 'binary':
    if len(given_number) != given_number.count('1') + given_number.count('0'):
        print('Invalid binary number input!')
        exit()
    result = 0
    needed_power = [x for x in range(len(given_number))] # 3,2,1,0
    needed_power.reverse()
    for num in given_number:
        result += int(num) * 2 ** int(needed_power[0])
        needed_power.remove(needed_power[0])
    print(result)

elif number_type == 'decimal':
    if given_number.startswith('0') and len(given_number) > 1:
        print('Invalid decimal number input!')
        exit()

    if int(given_number) == 0 and len(given_number) == 1:
        print(0)

    result = ''
    while int(given_number) > 0:
        current_number = int(given_number) # 18
        result += str(current_number % 2) # 0
        given_number = int(given_number) // 2

    for x in range(len(result) - 1, -1, -1):
        print(result[x], end='')
