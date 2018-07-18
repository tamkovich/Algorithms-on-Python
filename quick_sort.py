from random import randint


def quick_sort(array):
    if len(array) < 2:
        return array
    sep_ind = randint(0, len(array) - 1)
    sep = array[sep_ind]
    less = []
    greater = []
    for i in range(len(array)):
        if i != sep_ind:
            if array[i] <= sep:
                less.append(array[i])
            else:
                greater.append(array[i])
    return quick_sort(less) + [sep] + quick_sort(greater)


print(quick_sort([9, 3, 44, 3, 7, 5, 1, 7]))
print(quick_sort([5, 3, 6, 2, 10]))
