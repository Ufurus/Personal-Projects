""""
simple program to count word count in any form of a text file.
Just paste the text in the file and it will count the words in it.

Firstly, we create the file, next, we open it and paste the example text we need to calculate the words for it
After that, we make sure to calculate the words and miss the whitespaces.
"""

import os
import re

if os.path.exists("Sample_text.txt"):
    print("File already exists!")
else:
    with open("Sample_text.txt", "w") as file: # Creating the file if it doesn't exist yet.
        pass

with open("Sample_text.txt", "r") as second_file: # Creating a list of words that we can calculate the length of it.
    pattern = rf"\b\w+\b"
    text = second_file.read()
    found_words = re.findall(pattern, text)

# Final message to display word count.
print(f"In the current text file: {second_file.name}, there are exactly {len(found_words)} words total.")