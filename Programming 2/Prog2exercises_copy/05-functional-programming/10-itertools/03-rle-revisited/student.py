from itertools import groupby

def rle_encode(data):
    return ((key, len(list(group))) for key, group in groupby(data))
# it's way more easier and readable that the iterators themselves, it brought up a lot of confusion.

def rle_decode(data):
    return ''.join(char * count for char, count in data)
# lol