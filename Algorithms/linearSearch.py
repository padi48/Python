def linear_search(arr, item):
    for i in range(0, len(arr)):
        if item == arr[i]:
            return i 
    return -1 

arr = [1,3,5,6,7,11,13,15,17,18,19,22]
item = 22
result = linear_search(arr, item)

if result == -1:
    print("Element is not in array!")
else:
    print("Element is at index:", str(result))

