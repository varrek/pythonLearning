from collections import Counter, namedtuple

# O(n^2) ?
def get_missing_element_not_optimal(first_list, list_with_missing):
    for elem in first_list: # O(n^2)
        if elem not in list_with_missing:
            return elem
        list_with_missing.remove(elem)  # complexity of remove by itself is O(n)


# O(n)
def get_missing_element(first_list, list_with_missing):
    first_list_counter = Counter(first_list)  # O(n)
    second_list_counter = Counter(list_with_missing)  # O(n)
    result = first_list_counter - second_list_counter  # O(n)
    return list(result.keys())[0]  # O(n)


testdata_tuple = namedtuple('Testset', ['first_list', 'list_with_missing', 'result'])
test_data = [
    testdata_tuple([5, 5, 7, 7], [5, 7, 7], 5),
    testdata_tuple([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6], 5),
    testdata_tuple([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 5, 4, 3, 2, 1], 6)]

for data in test_data:
    result = get_missing_element(data.first_list, data.list_with_missing)
    assert (result == data.result)
