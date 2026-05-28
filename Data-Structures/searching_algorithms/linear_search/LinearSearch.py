def linear_search(arr , target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
        
    return -1

# Example usage
arr = [1, 2, 3, 4, 5]
target = 3  
result = linear_search(arr, target)
if result != -1:    
    print(f"Element found at index: {result}")      
else:
    print("Element not found in the array.")    