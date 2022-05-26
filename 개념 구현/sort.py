from typing import List

# 1. BubbleSort
test = [4, 6, 2, 9, 1]
def bubble_sort(lst: List) -> List:
    for _ in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]

    return lst


assert bubble_sort(test) == [1, 2, 4, 6, 9]


# 2. SelectionSort
test = [4, 6, 2, 9, 1]
def selection_sort(lst: List) -> List:

    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


assert selection_sort(test) == [1, 2, 4, 6, 9]

# 3. InsertionSort
test = [4, 6, 2, 9, 1]

def insertion_sort_1(lst: List) -> List:

    for i in range(len(lst)):
        for j in range(0, i+1):
            if lst[i] < lst[j]:
                lst.insert(j, lst.pop(i))

    return lst

print(insertion_sort_1(test))


# def insertion_sort(lst: List) -> List:
#
