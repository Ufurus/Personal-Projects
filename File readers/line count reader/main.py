# First iteration of line count reader. After entering file path, it will read all non whitespace lines, thus
# reading and counting the lines.

import os
import re

file_input = input('Enter file path: ') # putting the file path here
file_count_table = {}

not_file_count = 0
actual_file_count = 0

for file in os.listdir(file_input):

    # absolute path for the file for easier reading
    file_absolute_path = os.path.join(file_input, file)

    # checking if file is a text file
    if file.endswith(".txt"):
        actual_file_count += 1

    else:
        not_file_count += 1
        continue

    with open(file_absolute_path, 'r') as reading_file:
        count = len(reading_file.readlines())
        file_count_table[file] = count

print("----'File name': Line count----")
for key, value in file_count_table.items():
    print(f"'{key}': {value}")

if not_file_count > 0:
    print("----'File not count'----")
    print(not_file_count)