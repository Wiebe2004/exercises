import util

def group_by_suit(cards):
    return util.group_by(cards, lambda c1 : c1.suit)


def group_by_value(cards):
    return util.group_by(cards, lambda c1 : c1.value)


def partition_by_color(cards):
    black_suits = ['spades', 'clubs']
    red_suits = ['hearts', 'diamonds']
    return util.partition(cards, lambda c1 : c1.suit in black_suits)
    return util.partition(cards, lambda c2 : c2.suit not in red_suits)
    # I thought the util.py had everything implemented already.
    # Questions can be tricky, they we're asking to make a variable a list of colors.
