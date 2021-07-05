'''
All support indexing:

List []
Tuple (,)
String("")

memory stored in bits (8bits = 1 byte)
there's a memory address for each byte

Python represents UNICODE character with 16 bits (2 bytes)
SAMPLE is 6 characters = 12 bytes

If there's an existing list, and we create a new list referencing some of the
original lists items, it will just reference at the existing locations of those items.
New lists only change/create pointers, not duplicate objects in memory!
'''

import sys

n = 10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)

    print('Length : {0:2d}; Size in bytes: {1:4d}'. format(a,b))
    #Text formating: 2 integer spaces       4 integer spaces
    data.append(n)

