from typing import List
import heapq


# 1. BubbleSort
def bubble_sort(lst: List) -> List:
    for _ in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst


assert bubble_sort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert bubble_sort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]


# 2. SelectionSort
def selection_sort(lst: List) -> List:
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


assert selection_sort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert selection_sort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]


# 3. InsertionSort
def insertion_sort(lst: List) -> List:
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]

    return lst


def insertion_sort_1(lst: List) -> List:
    for i in range(1, len(lst)):
        cur = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > cur:
            lst[j+1] = lst[j]
            j -= 1

        lst[j + 1] = cur

    return lst


def insertion_sort_2(lst: List) -> List:

    for i in range(len(lst)):
        for j in range(0, i+1):
            if lst[i] < lst[j]:
                cur = lst.pop(i)
                lst.insert(j, cur)

    return lst


assert insertion_sort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertion_sort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]
assert insertion_sort_1([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertion_sort_1([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]
assert insertion_sort_2([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert insertion_sort_2([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]

# print(insertion_sort_1(test))


# def insertion_sort(lst: List) -> List:
#

# 4. QuickSort
def quick_sort(lst, start, end):
    if start >= end: return  # 원소가 1개인 경우
    pivot = start  # 피벗은 첫 요소
    left, right = start + 1, end

    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and lst[left] <= lst[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and lst[right] >= lst[pivot]:
            right -= 1
        if left > right:  # 엇갈린 경우
            lst[right], lst[pivot] = lst[pivot], lst[right]
        else:  # 엇갈리지 않은 경우
            lst[right], lst[left] = lst[left], lst[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(lst, start, right - 1)
    quick_sort(lst, right + 1, end)

    return lst


def partition(part_lst: List, pivot: int, end: int) -> int:
    i = pivot + 1
    j = end

    while True:
        while i < end and part_lst[i] < part_lst[pivot]:
            i += 1

        while j > pivot and part_lst[j] > part_lst[pivot]:
            j -= 1

        if j <= i:
            break

        part_lst[i], part_lst[j] = part_lst[j], part_lst[i]
        i += 1
        j -= 1

    part_lst[pivot], part_lst[j] = part_lst[j], part_lst[pivot]
    return j


def quicksort_1(lst: List, start: int, end: int) -> List:

    if start < end:
        pivot = partition(lst, start, end)
        quicksort_1(lst, start, pivot-1)
        quicksort_1(lst, pivot+1, end)

    return lst




quick_test = [5, 3, 8, 4, 9, 1, 6, 2, 7]
assert quick_sort(quick_test, 0, len(quick_test)-1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 5. Merge_sort
def merge_sort(lst: List) -> List:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L = lst[:mid]
    R = lst[mid:]

    return merge(merge_sort(L), merge_sort(R))


def merge(lst1: List, lst2: List) -> List:

    merged_lst = []
    i = j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged_lst.append(lst1[i])
            i += 1

        else:
            merged_lst.append(lst2[j])
            j += 1

    while i < len(lst1):
        merged_lst.append(lst1[i])
        i += 1

    while j < len(lst2):
        merged_lst.append(lst2[j])
        j += 1

    return merged_lst


assert merge_sort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert merge_sort([5, 3, 8, 4, 9, 1, 6, 2, 7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 6. HeapSort
def heap_sort(lst):
    result = []
    heapq.heapify(lst)
    for _ in range(len(lst)):
        result.append(heapq.heappop(lst))

    return result


heap_test = [5, 3, 8, 4, 9, 1, 6, 2, 7]
assert heap_sort(heap_test) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


