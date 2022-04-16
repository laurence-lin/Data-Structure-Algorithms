def selection_sort(list_):
    result = []
    small_test_value = list_[0]
    left_list = list_

    while len(left_list) > 1:

        for val in left_list:
            if val < small_test_value:
                small_test_value = val

        result.append(small_test_value)  # insert smallest value
        left_list.remove(small_test_value)  # remove smallest value from remain list
        small_test_value = left_list[0]

    return result


x = [1, 4, 2, 6, 4, 7, 65, 5, 8, 4]

result = selection_sort(x)
print(result)

