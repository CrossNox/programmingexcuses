from random import randint
import os.path

editions = {1:'Edition_1_1975.py',2:'Edition_2_1978.py',3:'Edition_3_1979.py',4:'Edition_4_1996.py'}

def get_strategy(edition='any'):
    """
    Returns a random strategy

    Args:
        edition: the edition that you wish to use. Can be either of:
            - 'any': a strategy from any edition will be returned
            - (1975 | 1): either way refers to the first edition
            - (1978 | 2): either way refers to the second edition
            - (1979 | 3): either way refers to the second edition
            - (1996 | 4): either way refers to the fourth edition
            Default value: 'any'
    Returns:
        A string with a uniformly chosen strategy
    """
    if edition not in ['any',]
    edition_number = randint(1,4)
    module = os.path.abspath(os.path.dirname(__file__))
    edition = os.path.join(module, editions[edition_number])
    with open(edition) as deck:
        cards = deck.readlines()
        card_number = randint(0,len(cards)-1)
        card = cards[card_number]
    return card
