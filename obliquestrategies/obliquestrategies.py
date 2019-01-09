from random import randint
import os.path

EDITIONS = {1: 'edition_1_1975.py',
            2: 'edition_2_1978.py',
            3: 'edition_3_1979.py',
            4: 'edition_4_1996.py'}

EDITIONS_ALIAS = {1975: 1, 1978: 2, 1979: 3, 1996: 4}


EDITION_1_LEN = 113
EDITION_2_LEN = 128
EDITION_3_LEN = 122
EDITION_4_LEN = 100
ALL_EDITIONS_LENS = [EDITION_1_LEN,
                     EDITION_2_LEN,
                     EDITION_3_LEN,
                     EDITION_4_LEN]


def get_strategy(edition='any'):
    """
    Returns a random strategy

    Args:
        edition: the edition that you wish to use. Can be either of:
            - 'any': a strategy from any edition will be returned
            - (1975 | 1): either way refers to the first edition from 1975
            - (1978 | 2): either way refers to the second edition from 1978
            - (1979 | 3): either way refers to the second edition from 1979
            - (1996 | 4): either way refers to the fourth edition from 1996
            Default value: 'any'
    Returns:
        A string with a uniformly chosen strategy
    """

    if edition in EDITIONS_ALIAS:
        edition = EDITIONS_ALIAS[edition]
    elif edition == 'any':
        seed = randint(1, sum(ALL_EDITIONS_LENS))
        for idx, _len in enumerate(ALL_EDITIONS_LENS):
            seed -= _len
            if seed <= 0:
                edition = idx + 1
                break
    elif edition not in EDITIONS:
        raise ValueError("Unknown edition: {}".format(edition))
    module = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(module, EDITIONS[edition])
    with open(filepath) as deck:
        card_number = randint(0, ALL_EDITIONS_LENS[edition - 1])
        for _ in range(1, card_number - 1):
            deck.readline()
        return deck.readline().strip()
