def selection_sort(integers_list):
    for i in range(len(integers_list)):
        min_index = i
        for index_unsorted in range(i + 1, len(integers_list)):
            if integers_list[index_unsorted] < integers_list[min_index]:
                min_index = index_unsorted

        integers_list[i], integers_list[min_index] = integers_list[min_index], integers_list[i]

    return integers_list

print(selection_sort([15, 11, 14, 13, 12, 42]))

# result -> [11, 12, 13, 14, 15, 42]
