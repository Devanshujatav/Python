def recurisve_binary_search(arr , start , end , target):
    # Base case
    if (start > end):
        return -1
    
    # mid element
    mid = start + (end - start) // 2

    # If the target is present at mid
    if (arr[mid] == target):
        return mid
    # If the target is smaller than mid, then search in the left subarray
    elif (arr[mid] > target):
        return recurisve_binary_search(arr , start , mid-1 , target)
    # If the target is greater than mid, then search in the right subarray
    else:
        return recurisve_binary_search(arr , mid+1 , end , target)
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input("Enter the target element: "))
result = recurisve_binary_search(arr , 0 , len(arr)-1 , target)

if (result != -1):
    print(f"Element found at index {result}")
else:
    print("Element not found")