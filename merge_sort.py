def msort(data1,data2):
    i,j = 0,0
    res = []
    while i < len(data1) and j < len(data2):
        if data1[i]< data2[j]:
            res.append(data1[i])
            i += 1
        else :
            res.append(data2[j]) 
            j += 1
    
    while j < len(data2):
        res.append(data2[j])
        j += 1
    while i < len(data1):
        res.append(data1[i])
        i+= 1
    
    return res

def merge_sort(arr):
    if len(arr)  < 2:
        return arr
    else :
        midle = len(arr)//2
        arr1 = merge_sort(arr[0:midle])
        arr2 = merge_sort(arr[midle: ])
        return msort(arr1,arr2)
    
