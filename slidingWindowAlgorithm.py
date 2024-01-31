# find the maximum sum of consequtive numbers which is k in list n

def maxSum(listarr,windowSize):
    arraySize = len(listarr)
    print("arraySize size is %d" % arraySize)
    if (arraySize <= windowSize):
        print("Invalid Operation")
        return -1
    window_sum = sum(listarr[i] for i in range(windowSize))
    print("window_sum is %d" % window_sum)
    maxSum = window_sum

    for i in range(arraySize-windowSize):
        window_sum = window_sum - listarr[i] + listarr[i+k]
        maxSum = max(window_sum, maxSum)
        print("maxSum at position i = %d" % i, maxSum)
        print("listarr[i] is %d" % listarr[i])
        print("listarr[i+k] is %d" % listarr[i+k])
        print("window_sum is %d" % window_sum)
    return maxSum

listarr = [80,-50,90,100]
k  = 2 #consequtive numbers count
result = maxSum(listarr, k)
print(result)