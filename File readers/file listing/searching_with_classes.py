import os; from pathlib import Path

""""
This is similar version to the recursive search one, as it uses recursive search here
but also uses classes to make objects of the files, with attributes for easier reading
"""

class File:
    def __init__(self, name, size, location):
        self.name = name
        self.size = size
        self.location = location

while True:
    destination = Path(input('Please enter path: '))
    if not os.path.exists(destination):
        print('Please enter a valid path')
    else: break

while True:
    number_of_files = input('Please enter number of files: ')
    if not number_of_files.isdigit():
        print('Please enter a valid number!')
    else: break

all_files = []
recursive_file_search_list = [p for p in destination.rglob("*") if p.is_file()]

for curr_file in recursive_file_search_list:
    file_size_kb = curr_file.stat().st_size / 1024
    file_size_mb = file_size_kb / 1024
    file_size_gb = file_size_mb / 1024
    if file_size_mb > 100 and file_size_gb < 1:
        curr_file = File(curr_file.name, f'{file_size_mb:.2f} MB', Path(curr_file).absolute())
        all_files.append(curr_file)
    if file_size_gb > 1:
        curr_file = File(curr_file.name, f'{file_size_gb:.2f} GB', Path(curr_file).absolute())
        all_files.append(curr_file)

filtered_files = sorted([x for x in all_files], key=lambda x: x.size)[0:int(number_of_files)]
for x in filtered_files:
    print(f"{x.name} - {x.size} - {x.location}")