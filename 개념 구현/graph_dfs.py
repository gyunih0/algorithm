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


def dfs_recursive(start_node: int, visited: List) -> List[int]:
    visited.append(start_node)

    for adj in graph[start_node]:
        if adj not in visited:
            dfs_recursive(adj, visited)

    return visited


def dfs_stack(start_node: int) -> List[int]:
    visited = []
    stack = [start_node]

    while stack:
        top = stack.pop()
        visited.append(top)

        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)
