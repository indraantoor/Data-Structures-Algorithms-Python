nums = [5, 2, 9, 1, 5, 6]


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort(arr):
    for element in arr:
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                swap(arr, index, (index + 1))


# Test

print("Pre-Sort: {0}".format(nums))
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))