import string

def get_idx_naive(word):
    # O(N^2)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]  # b a e k j o o n
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]  # a b c d e f g ..
            if result[j] == -1 and char == lo:
                result[j] = i
    print(' '.join([str(num) for num in result]))


def get_idx(word):
    # point 1. ord
    # point 2. O(n^2) -> O(n)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))

word = "baekjoon"

get_idx_naive(word)
get_idx(word)

a = 1
print(a.lower())






