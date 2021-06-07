arr = [1,0,2,3,0,4,5,0]


def move_zeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            i += 1
        i += 1
    return arr


print(move_zeros(arr))
