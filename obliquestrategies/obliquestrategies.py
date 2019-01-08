from random import randint
import os.path

editions = {1:'Edition_1_1975.py',2:'Edition_2_1978.py',3:'Edition_3_1979.py',4:'Edition_4_1996.py'}

def get_strategy():
    edition_number = randint(1,4)
    module = os.path.abspath(os.path.dirname(__file__))
    edition = os.path.join(module, editions[edition_number])
    with open(edition) as deck:
        cards = deck.readlines()
        card_number = randint(0,len(cards)-1)
        card = cards[card_number]
    return card