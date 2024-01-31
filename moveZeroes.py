def moveZeros(listarr):
    j = 0
    for num in listarr:
        if (num != 0):
            listarr[j] = num
            j += 1
        # print(listarr)
    for x in range(j, len(listarr)):
        listarr[x] = 0
        # print(listarr)
    return listarr


listarr = [0, 20, 340, 563, 0, 25, 36, 0, 78, 0, 12]
result = moveZeros(listarr)
print(result)
