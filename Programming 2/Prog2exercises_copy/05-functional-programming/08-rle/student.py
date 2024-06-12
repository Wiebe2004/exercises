def rle_encode(data):
    encoding = []
    data = iter(data)
    try:
        current = next(data)
        count = 1
        while True:
            try:
                new = next(data)
                if new == current:
                    count += 1
                else:
                    encoding.append((current, count))
                    current = new
                    count = 1
            except StopIteration:
                encoding.append((current, count))
                break
    except StopIteration:
        pass
    return encoding


def rle_decode(data):
    decoding = ''
    for count, value in data:
        decoding += value * count
    return decoding