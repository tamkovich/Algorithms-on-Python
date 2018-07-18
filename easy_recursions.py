def summary(arr):  # the same as base func sum
    if not arr:  # if len(arr) == 0:  # if count(arr) == 0:
        return 0
    return arr[0] + summary(arr[1:])


def count(arr):  # the same as base func len
    if not arr:
        return 0
    return 1 + count(arr[1:])


def find_max(arr):  # the same as base func max
    if not arr:
        return 0
    guess = find_max(arr[1:])
    return arr[0] if arr[0] > guess else guess


arr = [1, 5, 6, 7, 8, 11, 56]
# arr = [9, 3, 44, 3, 7, 5, 1, 7]
# arr = [5, 3, 6, 2, 10]
print(summary(arr), 'summary = sum', sum(arr))
print(count(arr), 'count = len', len(arr))
print(find_max(arr), 'find_max = max', max(arr))
