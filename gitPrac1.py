def summer69(arr):
    sum = 0
    i = 0
    size = len(arr)
    while i < size:
        if arr[i] == 6:
            while arr[i] != 9:
                i += 1
        elif arr[i] == 9:
                i += 1
        else:
            sum += arr[i]
            i += 1
    return sum
if __name__ == '__main__':
    sum = summer69([4, 5, 6, 7, 8, 9, 10])
    print("sum = " + str(sum))