import numpy as np
from typing import List
import time

# Binary search: the fastest search alrogithm in most cases
# Require the search list to be sorted

def mid_val(list_):
    mid_ind = len(list_)//2
    if len(list_)%2 == 0:
        return (list_[mid_ind - 1] + list_[mid_ind])/2
    else:
        return list_[mid_ind]

def binary_search(list_: List, value):
    # If not exist, return -1

    list_ = sorted(list_)
    while (mid_val[list_] != value): 

    return -1


search_list = [1, 5, 3, 5, 6, 7, 8, 4, 5, 6, 9, 10]
value_1 = 9

start = time.time()
result = binary_search(search_list, value_1)
end = time.time()


print("Search result: ", result)
print("Time cost: ", (end - start))

