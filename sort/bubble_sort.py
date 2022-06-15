

from os import TMP_MAX


raw_list = [-3, 6, 5, -1, 0, 9, 3]
sorted_list = []

remain_list = raw_list.copy()

while len(remain_list) > 1:
    for i in range(len(remain_list) - 1):
        if remain_list[i] > remain_list[i+1]: # if left > right, switch value
            tmp = remain_list[i] 
            remain_list[i] = remain_list[i+1]
            remain_list[i+1] = tmp

    sorted_list.append(remain_list[-1])
    remain_list.pop() # drop the max value from remain list

print("Origin list:", raw_list)
print("Sorted list:", sorted_list[::-1])

