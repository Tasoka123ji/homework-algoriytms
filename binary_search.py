def binary_search_recursion(arr: list, target: int,lenght = None) -> int:
    mid =  len(arr)//2
    
    if not lenght:
        lenght = mid    
            
    if target == arr[mid]:
        return lenght
    if mid == 1 or mid == 0:
        return False 
    
    if target < arr[mid]:
        return binary_search(arr[:mid+1],target,lenght - len(arr)//4)
    
    if target > arr[mid]:
        return binary_search(arr[mid:],target,lenght+len(arr)//4)
   
    

def binary_search(arr,target):
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        
        mid = (left + right)//2
        
        if target ==  arr[mid]:
            return mid 
        
        if target > arr[mid]:
            left = mid + 1
        
        if target < arr[mid]:
            right = mid - 1
            
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

print(binary_search(arr,6))