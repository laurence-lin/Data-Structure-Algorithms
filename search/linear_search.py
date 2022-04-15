import numpy as np
from typing import List
import time

# Linear search, or Sequential search
# Search elements one by one, the list to search need not to be sorted
# Time complexity: O(N)


def linear_search(list_: List, value):
    # list_: list to search for
    # value: value to search in the list
    # return: index where the value locate in list. If not found, return -1

    for i in range(len(list_)):
        if value == list_[i]:
            return i

    return -1


search_list = [1, 5, 3, 5, 6, 7, 8, 4, 5, 6, 9, 10]
value_1 = 9

start = time.time()
result = linear_search(search_list, value_1)
end = time.time()

print("Search result: ", result)
print("Time cost: ", (end - start))

