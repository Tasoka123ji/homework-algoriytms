def maximum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0]> arr[1] else arr[1]
    if arr[0] > arr[1]:
        arr[1] = arr[0]
    return maximum(arr[1:])
 
def minimum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0]< arr[1] else arr[1]
    if arr[0] < arr[1]:
        arr[1] = arr[0]
    return minimum(arr[1:]) 

k = [1,2,3,4,90,6,7,8,9]
print(maximum(k))

        
