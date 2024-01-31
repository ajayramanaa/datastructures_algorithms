# This program uses Binary Search algorithm
def binarySearch(listarr, target):
    print("Binary Search")
    left = 0
    right = len(listarr)-1
    print(right)

    while (left <= right):
        mid = (left+right)//2
        if (listarr[mid] == target):
            return mid
        elif (listarr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return -1


listarr = [27, 10, 35, 89, 105, 77, 87, 38]
# Binary search list should be in sorted order.
listarr.sort()
print(listarr)
target = 77
result = binarySearch(listarr, target)
if result != -1:
    print("target found at %d" % result)
else:
    print("target not found")
