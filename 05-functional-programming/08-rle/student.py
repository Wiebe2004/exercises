# def rle_encode(data):
#     encoding = ''
#     i = 0
#     while i < len(data):
#         count = 1
#         while i + 1 <len(data) and data[i] == data[i+1]:
#             i += 1
#             count += 1
#         encoding += str(count) + data[i]
#         i += 1

#     return encoding

# # print(rle_encode("WWWWAAAASSABBII"))


# def rle_decode(data):
#     decoding = ''
#     i = 0
#     while i < len(data):
#         count = int(data[i])
#         char = data[i + 1]
#         decoding += char * count
#         i+= 2
#     return decoding

# # print(rle_decode(rle_encode("WWWWAAAASSABBII")))


def rle_encode(data):
    data = iter(data)
    try:
        last_datum = next(data)
        count = 1
        for datum in data:
            if last_datum == datum:
                count += 1
            else:
                yield (last_datum, count)
                last_datum = datum
                count = 1
        yield (last_datum, count)
    except StopIteration:
        pass


def rle_decode(data):
    for datum, count in data:
        for _ in range(count):
            yield datum
