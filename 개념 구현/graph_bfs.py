from collections import deque
from typing import List
## BFS

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def bfs(start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited

print(bfs(1))

def bfs_mine(start: int) -> List[int]:
    visited = []
    q = deque([start])

    while q:
        node = q.popleft()
        visited.append(node)
        for adj in graph[node]:
            if adj not in visited and adj not in q:
                q.append(adj)

    return visited

print(bfs_mine(1))


def bfs_extends(start: int) -> List[int]:
    visited = []
    q = deque([])

    q.append(start)

    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])

    return visited


print(bfs_extends(1))


