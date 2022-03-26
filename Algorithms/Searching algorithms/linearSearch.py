arr = [2, 1, 22, 14, 19, 43, 28, 36, 17]
item = 43

#non-recursive version
def linearSearch(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    
    return -1

result = linearSearch(arr, item)
if result != -1:
    print("Item found at index:", result)

#recursive version
def recursiveLinear(arr, item, left, right):
    if right < left:
        return -1
    if arr[left] == item:
        return left
    if arr[right] == item:
        return right
    return recursiveLinear(arr, item, left+1, right-1)

x = recursiveLinear(arr, item, 0, len(arr) - 1)
if x != -1:
    print("Item found at index:", x)
