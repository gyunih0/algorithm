from typing import List

"""
N-Queen (Back tracking)
https://www.acmicpc.net/problem/9663
"""

def nqueen(num: int):

    visited = [-1] * num
    cnt = 0
    answers = []

    def dfs(row):
        if row >= num:
            nonlocal cnt
            cnt += 1
            print("*" * 80)
            print(f"{cnt}번째 답 - visited: {visited}")
            grid = [['.'] * num for _ in range(num)]
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                print(row)
                result.append(''.join(row))
            answers.append(result)
            ################
            return

        for col in range(num):
            visited[row] = col
            if is_ok_on(row):
                dfs(row + 1)

    def is_ok_on(nth_row):
        for row in range(nth_row):
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False

        return True

    dfs(0)
    return answers


nqueen(4)