def merge_sort(list_):
    # By default, sort from small to large
    # divide & conquer
    # front: start index of list_
    # end: end index of list_
    if len(list_) > 1:  # if input array length > 1, do merge sort, else do nothing
        mid = len(list_) // 2
        left_arr = list_[:mid]  # divide current array from middle
        right_arr = list_[mid:]
        # sort left array & right array
        merge_sort(left_arr)
        merge_sort(right_arr)

        left_ind = 0
        right_ind = 0
        merge_ind = 0
        # Smallest unit: len(right_arr)=1, len(left_arr)=1
        # 1. Compare the first element for left & right array, insert to result sorted list
        while right_ind < len(right_arr) and left_ind < len(
            left_arr
        ):  # right_ind set within right_arr, left_ind set within left_arr
            if (
                right_arr[right_ind] < left_arr[left_ind]
            ):  # get the smaller value of first element in left_arr & right_arr
                list_[merge_ind] = right_arr[right_ind]  # insert the smaller value to result list
                right_ind += 1  # move on to next right element

            else:
                list_[merge_ind] = left_arr[left_ind]
                left_ind += 1

            merge_ind += 1  # Move on to next location to insert

        # After 1., it would then go to either 2. OR 3.
        # 2. If right array remains element to insert
        while right_ind < len(right_arr):
            list_[merge_ind] = right_arr[right_ind]
            right_ind += 1
            merge_ind += 1

        # 3. If left array remains element to insert
        while left_ind < len(left_arr):
            list_[merge_ind] = left_arr[left_ind]
            left_ind += 1
            merge_ind += 1


val_list = [1, 5, 3, 6, 7, 5, 4, 6, 8, 3]

merge_sort(val_list)

print(val_list)
