# Quick Sort

# Using randrange to generate a random index
from random import randrange


def quicksort(list, start, end):
    if start >= end:
        return list
    # pivot_idx is a random index between start and end
    # Random protect's our code from insufficient runtime
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    lesser_than_pointer = start
    for index in range(start, end):
        if list[index] < pivot_element:
            list[lesser_than_pointer], list[index] = list[index], list[lesser_than_pointer]
            lesser_than_pointer += 1
            list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
    print(list[start])
    start += 1
    return quicksort(list, start, end)


my_list = [52, 209, 18]
print("Before Sort: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("After Sort: ", sorted_list)
