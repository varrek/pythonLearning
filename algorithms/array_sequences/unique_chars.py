from collections import namedtuple


def is_all_unique_chars(input_s):
    return len(set(input_s)) == len(input_s)


def is_all_unique_chars_2(input_s):
    l = []
    for sym in input_s:
        if sym in l:
            return False
        l.append(sym)

    return True


testdata_tuple = namedtuple('Testset', ['string', 'result'])
test_data = [
    testdata_tuple('', True),
    testdata_tuple('goo', False),
    testdata_tuple('abcdefg', True)]

for data in test_data:
    result = is_all_unique_chars_2(data.string)
    assert (result == data.result)
