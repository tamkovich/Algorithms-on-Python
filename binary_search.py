def binary_search(l, item):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        variant = l[mid]
        if item == variant:
            return mid
        elif item < variant:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursion(l, item, increase):
    low = 0
    high = len(l) - 1
    if low > high:
        return None
    mid = (low + high) // 2
    variant = l[mid]
    if item == variant:
        return mid + increase
    elif item < variant:
        high = mid - 1
        return binary_search_recursion(l[low:high + 1], item, increase)
    else:
        low = mid + 1
        return binary_search_recursion(l[low:high + 1], item, low + increase)


a = [1, 5, 6, 7, 8, 11, 56]
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
item = int(input('Enter the item which you wanna to find in the existing list: '))
print('Cycle = ', binary_search(a, item))
print('Recursion = ', binary_search_recursion(a, item, 0))
