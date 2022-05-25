import heapq
from typing import List

# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# solution

def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    min_heap = []
    answer = []
    heapq.heapify(min_heap)

    for i in range(len(mat)):
        heapq.heappush(min_heap, (mat[i].count(1), i))

    while k != 0:
        val, row = heapq.heappop(min_heap)
        answer.append(row)
        k -= 1
    return answer


mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]

print(kWeakestRows(mat,3))