from data_gathering import information_getter

print('*' * 3, 'STEAM PERSONAL DATA', '*' * 3)
print('Please choose data type to show, available data types are:\n-ACHIEVEMENTS\n-MATCH HISTORY')

chosen_type = input('Please enter data type: ').lower()
while chosen_type != 'achievements' and chosen_type != 'match history':
    print('Wrong data type! Please enter a valid one.')
    chosen_type = input('Please enter data type: ').lower()

information_getter(chosen_type)