def check_sorted_array(arr , index = 0):
    # Base case
    if (index == len(arr)-1):
        return True
    
    # If an element is greater to the next element 
    if (arr[index] > arr[index+1]):
        return False
    
    # Recursive call for the next element
    return check_sorted_array(arr, index+1)

list = [10, 2, 3, 4, 5]
if (check_sorted_array(list)):
    print("The array is sorted.")
else:    
    print("The array is not sorted.")
