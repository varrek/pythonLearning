from collections import namedtuple


def get_compressed_string(input_s):
    result = ''
    prev_s = ''
    if len(input_s) == 0:
        return input_s
    count = 0
    for sym in input_s:
        if sym == prev_s:
            count += 1
        else:
            result += str(count) if count > 0 else ''
            result += sym
            prev_s = sym
            count = 1
    result += str(count)
    return result


testdata_tuple = namedtuple('Testset', ['input', 'result'])
test_data = [
    testdata_tuple('AABBCC', 'A2B2C2'),
    testdata_tuple('AAABCCDDDDD', 'A3B1C2D5'),
    testdata_tuple('AAAABBBBCCCCCDDEEEE', 'A4B4C5D2E4'),
    testdata_tuple('A', 'A1'),
    testdata_tuple('AAB', 'A2B1'),
    testdata_tuple('AAaa', 'A2a2'),
    testdata_tuple('', '')]

for data in test_data:
    result = get_compressed_string(data.input)
    assert (result == data.result)
