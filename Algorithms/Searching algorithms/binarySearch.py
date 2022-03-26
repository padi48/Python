arr = [1, 3, 5, 11, 13, 15, 22, 25]
item = 3
#non-recursion version
def binarySearch(arr, item):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == item:
            return middle
        elif arr[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
    return -1

found = binarySearch(arr, item)

if found != -1:
    print("Item found at index:", found)
else:
    print("Item not found in array!")

#recursive version
def recursiveBindary(arr, left, right, item):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return recursiveBindary(arr, mid + 1, right, item)
    else:
        return recursiveBindary(arr, left, mid - 1, item)

x = recursiveBindary(arr, 0, len(arr) - 1, 15)
if x != -1:
    print("Item found at index:", x)
else:
    print("Item not found in array!")
