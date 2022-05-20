from collections import deque

from typing import List

'''
No.1260  BFS와 DFS
https://www.acmicpc.net/problem/1260
'''


def dfs(start: int) -> List[int]:
    visit = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visit:
            visit.append(node)
            stack.extend(reversed(graph[node]))

    return visit


def bfs(start: int) -> List[int]:
    visit = []
    q = deque([])

    q.append(start)

    while q:
        node = q.popleft()
        if node not in visit:
            visit.append(node)
            q.extend(graph[node])

    return visit




graph = {}

inputs = list(map(int, input().split()))
for i in range(1, inputs[0]+1):
    graph[i] = []

for i in range(1, inputs[1]+1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, len(graph)+1):
    graph[i].sort()


start = inputs[2]

dfs_result = dfs(start)
bfs_result = bfs(start)
dfs_answer = ''
bfs_answer = ''

for result in dfs_result:
    dfs_answer += ' {}'.format(result)


for result in bfs_result:
    bfs_answer += ' {}'.format(result)

print(dfs_answer.strip() + "\n" + bfs_answer.strip())
