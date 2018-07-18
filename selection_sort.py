def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for index, val in enumerate(arr):
        if val < smallest:
            smallest_index = index
            smallest = val
    return smallest_index


def selection_sort(arr):
    res = []
    while arr:
        res.append(arr.pop(find_smallest(arr)))  # The same as two lines below
        # smallest_index = find_smallest(arr)
        # res.append(arr.pop(smallest_index))
    return res


print(selection_sort([9, 3, 44, 3, 7, 5, 1, 7]))
print(selection_sort([5, 3, 6, 2, 10]))
