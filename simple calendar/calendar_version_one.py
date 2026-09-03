third_group = ['february'] # 28

ordered_months = ['january','february', 'march', 'april',
                  'may', 'june', 'july', 'august', 'september','october', 'november','december']
""""
Simple calendar using for loops and lists.
"""

for month in ordered_months:
    if month in first_group:
        for day in range(1, 31 + 1):
            print(f"{month} - {day}")
    elif month in second_group:
        for day in range(1, 31):
            print(f"{month} - {day}")
    elif month in third_group:
        for day in range(1, 29):
            print(f"{month} - {day}")
