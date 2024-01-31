# find max and min of sum of 4 numbers in an array

def findmaxmin(arr):
    maxnumber = 0
    minnumber = 9999999999999
    n = len(arr)
    s = 0
    for i in range(n):
        s += arr[i]
        minnumber = min(minnumber, arr[i])
        maxnumber = max(maxnumber, arr[i])
    print(s-minnumber, s-maxnumber)

arr = [2,3,4,5,6]
findmaxmin(arr)

