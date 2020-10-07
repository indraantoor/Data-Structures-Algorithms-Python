# Merge Sort
# Uses Recursion


def merge_sort(items):
    if len(items) <= 1:
        return items
    # Separation Logic
    middle_index = len(items) // 2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    # Logic To Make This Function Return A Sorted List
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    # Divide And Conquer Concept
    while left and right:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    # Checking If There Are Still Any Leftover Elements
    if left:
        result += left
    if right:
        result += right
    return result
