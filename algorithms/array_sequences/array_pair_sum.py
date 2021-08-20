# given an array, output all the unique pairs that sum up to specific value k
# pair_sum([1,3,2,2], 4)
# returns (1, 3) and (2, 2)
from typing import List
from collections import namedtuple

# 0(n^2)
# @TODO: use set for O(n)
def pair_sum(array_to_check: List, k: int):
    result = []
    l = len(array_to_check)
    for i in range(l):
        number = array_to_check[i]
        for j in range(l):
            another_number = array_to_check[j]
            if i == j:
                continue
            if number + another_number == k:
                pair = tuple(sorted((number, another_number)))
                if not pair in result:
                    result.append(pair)

    return result


testdata_tuple = namedtuple('Testset', ['list_to_check', 'number', 'result'])
test_data = [
    testdata_tuple([1,3,2,2], 4, [(1, 3), (2, 2)]),
    testdata_tuple([1,2,3,1], 3, [(1, 2)]),
    testdata_tuple([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10, [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (-1, 11)])
]

for data in test_data:
    result = pair_sum(data.list_to_check, data.number)
    assert (result == data.result)