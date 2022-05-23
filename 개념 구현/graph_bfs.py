from collections import deque
from typing import List

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
    q = deque([])

    q.append(start)
    while q:
        if not graph[q[0]]:
            visited.append(q.popleft())
        else:
            for adj in graph[q[0]]:
                if adj not in visited:
                    visited.append(q.popleft())
                    q.append(adj)
        print(q)

    return visited

print(bfs_mine(1))


def bfs_extend(start: int) -> List[int]:
    visited = []
    q = deque([])

    q.append(start)

    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])

    return visited


print(bfs_extend(1))


