from typing import List
from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def dfs_recursive(start_node: int, visited: List) -> List[int]:

    visited.append(start_node)

    for adj in graph[start_node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited


def dfs_stack(start: int) -> List[int]:
    visited = []
    stack = []

    stack.append(start)
    while stack:
        node = stack.pop()
        visited.append(node)

        for adj in graph[node]:
            if adj not in visited:
                stack.append(adj)

    return visited



def dfs_mine(start: int) -> List[int]:
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited

for i in range(1, len(graph)+1):
    graph[i].sort()

print(dfs_recursive(1,[]))
print(dfs_stack(1))
print(dfs_mine(1))