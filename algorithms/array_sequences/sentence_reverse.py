from collections import namedtuple


def get_reversed_sentence(input_s):
    l = input_s.split()
    result = ' '.join(reversed(l))
    return result


def get_reversed_sentence_cycle(input_s):
    space = ' '
    l = len(input_s)
    res_list = []
    i = 0
    while i < l:
        if (input_s[i]) != space:
            pos_start = i
            while i < l and input_s[i] != ' ':
                i +=1
            res_list.append(input_s[pos_start:i])
        i+=1
    return ' '.join(res_list[::-1])


testdata_tuple = namedtuple('Testset', ['input', 'result'])
test_data = [
    testdata_tuple('    space before', 'before space'),
    testdata_tuple('space after     ', 'after space'),
    testdata_tuple('   Hello John    how are you   ', 'you are how John Hello'),
    testdata_tuple('1', '1')]


for data in test_data:
    result = get_reversed_sentence_cycle(data.input)
    assert (result == data.result)
