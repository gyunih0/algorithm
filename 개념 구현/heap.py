import heapq
from typing import List


class MaxHeap:
    def __init__(self):
        # 힙은 계산 편의를 위해 index를 1부터 부여한다.
        self.items = [None]

    def insert(self, item):
        self.items.append(item)
        self.up_heap()

    def up_heap(self):
        cur = len(self.items) - 1
        # 부모의 index = (자식의 index) // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

                cur = parent
                parent = cur // 2

    def extract(self):
        if len(self.items) - 1 < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self.down_heap(1)

        return root

    def down_heap(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self.items) - 1 and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self.items) - 1 and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self.down_heap(biggest)




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