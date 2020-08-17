if __name__ == '__main__':
    n = int(input())

    if(n < 2 or n > 10):
        n = int(input("Enter between 2 and 10: "))
    else:
        arr = list(set(map(int, input().split())))

    # largest = max(arr)
    # arr1 = set(arr)
    # arr=list(arr1)
    #
    # for i in range(len(arr)):
    #     if arr[i] == largest:
    #         arr.remove(max(arr))
    arr.sort(reverse=True)

print(arr[1])
