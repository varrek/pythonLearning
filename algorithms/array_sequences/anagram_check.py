# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.[1] For example, the word anagram itself
# can be rearranged into nag a ram, also the word binary into brainy and the word adobe into abode.
from collections import Counter
from collections import namedtuple


def is_anagram(sentence1: str, sentence2: str) -> bool:
    sentence1 = sentence1.lower().replace(' ', '')
    sentence2 = sentence2.lower().replace(' ', '')
    count_sentence_1 = Counter(sentence1)
    count_sentence_2 = Counter(sentence2)

    return count_sentence_1 == count_sentence_2


anagram = namedtuple('Testset', ['sentence1', 'sentence2', 'isAnagram'])
test_sentences = [anagram('public relations', 'crap built on lies', True),
                  anagram('clint eastwood', 'old west action', True),
                  anagram('Dormitory', 'Dirty room', True),
                  anagram('Listen', 'Silent', True),
                  anagram('Rest', 'Test', False),
                  anagram('aabbcc', 'aabbc', False),
                  anagram('123', '2 2', False),
                  anagram('go go go', 'gggooo', True),
                  anagram('go go goo', 'gggooo', False)]


for sentence in test_sentences:
    result = is_anagram(sentence.sentence1, sentence.sentence2)
    assert (result == sentence.isAnagram)
