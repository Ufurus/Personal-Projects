import re

print("Enter a text here and this will count how many words are in this text.")
my_text = input("Enter your text here: ")
word_count = r"\w+"
result = len(re.findall(word_count, my_text))
print(f"There are {result} words in this text!")