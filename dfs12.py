from typing import List

def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


def letterCombinations(digits: str) -> List[str]:
    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
           '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []

    def dfs(index, path):

        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):  # 시작 다음 부터 모든 digits에 대해서
            for char in dic[digits[i]]:  # 해당 하는 digits의 문자에 대해
                dfs(i + 1, path + char)  # path에 더해준다

    dfs(0, "")

    return result



def letterCombinations_2(digits):
    dictionary = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []
    if len(digits) == 0:
        return result
    dfs(digits, 0, dictionary, '', result)
    return result


def dfs(nums, index, dictionary, path, result):
    if index == len(nums):
        result.append(path)
        return
    letters = dictionary[nums[index]]
    for letter in letters:
        dfs(nums, index + 1, dictionary, path + letter, result)



print(letterCombinations_2('234'))



def permute(nums: List[int]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)

            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results

print()

def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


