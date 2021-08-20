from collections import namedtuple


def get_largest_continious_sum(list_i):
    l = len(list_i)
    sums = []
    for i in range(l):
        elem_sums = []
        j = i
        while j < l:
            if i == j:
                elem_sums.append(list_i[i])
            else:
                elem_sums.append(sum(list_i[i:j]))
            j = j+1
        sums.append(max(elem_sums))
    result = max(sums)
    return result


testdata_tuple = namedtuple('Testset', ['list',  'result'])
test_data = [
    testdata_tuple([1,2,-1,3,4,-1],9),
    testdata_tuple([1,2,-1,3,4,10,10,-10,-1],29),
    testdata_tuple([-1,1],1)]


for data in test_data:
    result = get_largest_continious_sum(data.list)
    assert (result == data.result)