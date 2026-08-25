# unlocked/locked achievements count
with open('data.json') as file:

    lines = file.readlines()
    unlocked_count = 0
    locked_count = 0
    for line in lines:
        if line.startswith('achievement'):
            if line.split()[3].replace(',', '') == '1':
                unlocked_count += 1
            else:
                locked_count += 1
    print(f'Unlocked achievements count: {unlocked_count}')
    print(f'Locked achievements count: {locked_count}')

