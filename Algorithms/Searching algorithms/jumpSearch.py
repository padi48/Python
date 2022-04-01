from math import sqrt

arr = [1, 3, 5, 9, 11, 15, 23, 24, 34, 44, 45, 46]
item = 46

def linear(block, item, p):
    for i in range(len(block)):
        if block[i] == item:
            return i + p
        i += 1

    return -1

def jumpSearch(arr, item):
    n = len(arr)
    m = int(sqrt(n))
    p = 0

    while p != n-1 and p < item:
        if arr[p + m-1] == item:
            return p + m-1
        elif arr[p + m-1] > item:
            block = arr[p: p + m-1]
            return linear(block, item, p)
        p += m

    block = p + m-1
    return linear(block, item, p)

result = jumpSearch(arr, item)
if result != -1:
    print("Item found at index:", result)
