from typing import List
import collections

# 6 - 1
def isPalindrome1(s: str) -> bool:
    # 리스트 이용
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    for i in range(len(strs)):
        if strs[i] != strs[-(i+1)]:
            return False

    return True


# 6 - 2
# two pointer
def reverseString1(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# pythonic way
def reverseString2(s: List[str]) -> None:
    s.reverse()
    # s[:] = s[::-1]


# 5
# sort -> dic
test_words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# pythonic way
def groupAnagrams(words: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)  # dic 선언

    for word in words:
        anagrams[''.join(sorted(word))].append(word)
        print(anagrams)

    return list(anagrams.values())


def groupAnagrams2(words: List[str]) -> List[List[str]]:
    results = {}  # key = sorted word, value = given word
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in results.keys():
            results[sorted_word] = []
            results[sorted_word].append(word)
        else:
            results[sorted_word].append(word)

    return list(results.values())


# 6
test_words = 'babad'
def longestPalindrome(s: str) -> str:

    def expand(left, right): #
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # 하나씩 더 간거 빼줘야함

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
    return result


print(longestPalindrome(test_words))
