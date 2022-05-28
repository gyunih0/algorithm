from typing import List
import bisect


# https://leetcode.com/problems/binary-search/
def binary_search(nums: List[int], target: int) -> int:

    def bs(start: int, end: int) -> int:

        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] > target:
            return bs(start, mid - 1)

        elif nums[mid] < target:
            return bs(mid + 1, end)

        else:
            return mid

    return bs(0, len(nums)-1)


def binary_search_using_bisect(nums, target):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index

    else:
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9

assert binary_search_using_bisect(nums, target) == 4

assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert binary_search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
