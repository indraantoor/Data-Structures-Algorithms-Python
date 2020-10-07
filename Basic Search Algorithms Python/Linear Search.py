# Linear search


def linear_search(search_list, target_value):
    for index in range(len(search_list)):
        print(search_list[index])
        if search_list[index] == target_value:
            return index
    # Raising value error using string interpolation
    raise ValueError("{0} not in list".format(target_value))


values = [54, 22, 46, 99]
print(linear_search(values, 12))

# Linear search with exception handling (try/except)

number_list = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]
target_number = 33


def linear_search(search_list, target_value):
    for index in range(len(search_list)):
        if search_list[index] == target_value:
            return index
    raise ValueError("{0} not in list".format(target_value))


try:
    result = linear_search(number_list, target_number)
    print(result)
except ValueError as error_message:
    print("{0}".format(error_message))

try:
    result = linear_search(number_list, 800)
    print(result)
except ValueError as error_message:
    print("{0}".format(error_message))