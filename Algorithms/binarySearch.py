def binary_search(arr, item):
    start_index = 0
    end_index = len(arr) - 1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2

        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            end_index = mid - 1
        else:
            start_index = mid + 1

    return None

arr = [1,3,6,7,8,11,13,15,17,18]
item = 11
result = binary_search(arr, item)

if result == None:
    print("Element is not present in array")
else:
    print("Element is at index:", str(result))

