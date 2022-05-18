from typing import List
# 11 - 29 jewels and stones
import collections

freqs = {}

S = 'aAAbbbb'
for char in S:
    if char not in freqs:
        freqs[char] = 1
    else:
        freqs[char] += 1


def numJewelsInStones_1(J: str, S: str) -> int:
    hash_table = {}
    count = 0

    for char in S:
        if char not in hash_table:
            hash_table[char] = 1
        else:
            hash_table[char] += 1

    for char in J:
        if char in hash_table:
            count += hash_table[char]

    return count


def numJewelsInStones_2(J: str, S: str) -> int:

    return sum([s in J for s in S])
# List comprehension
# [s for s in S] -> ['a', 'A', 'A', 'b', 'b', 'b', 'b']
# [s in J for s in S] -> [True, True, True, False, False, False, False]

# J = 'aA'
# S = 'aAAbbbb'
#
# print(numJewelsInStones_2(J, S))
#


# 11 - 30

# 11 - 31
def topKFrequent(nums: List[int], k: int) -> int:
    pass

def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    max_length = start = 0