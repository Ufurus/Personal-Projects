import random

def random_word(words):
    return random.choice(words)

name_list = ["Ivan", "John", "George", "Alex", "Toshko"]
places = ["Sofia", "Pleven", "Kaspichan", "Kazanluk", "Qmbol"]
verbs_list = ["eats", "holds", "sees", "plays with", "brings"]
noun_list = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park", "near the city"]

while True:
    random_name = random_word(name_list)
    random_place = random_word(places)
    random_verb = random_word(verbs_list)
    random_noun = random_word(noun_list)
    random_adverb = random_word(adverbs)
    random_detail = random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    action = input("Press [ENTER] to generate a new sentence! Or type [exit] if you want to stop!")
    if action == "exit":
        print("play again!")
        break
