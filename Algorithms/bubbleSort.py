import time

t = time.perf_counter()
def bubble_sort(a_list):
    i = len(a_list) - 1 
    s = False

    while not s:
        s = True
        for x in range(0, i):
            if a_list[x] > a_list[x+1]:
                s = False
                a_list[x+1], a_list[x] = a_list[x], a_list[x+1]

    return a_list    

print(bubble_sort([2,5,3,11,13,6,7,8,1,10]))
print(t)

x = time.perf_counter()
def bubble2(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble2([2,5,3,11,13,6,7,8,1,10]))
print(x)
