def inserion_sort(arr):
    l = len(arr)
    for i in range (1,l):
        while arr[i] < arr[i-1] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i-=1
    return arr