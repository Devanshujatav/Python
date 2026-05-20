def array_sum(arr , index):
    #Base Case
    if index == len(arr):
        return 0
    
    # Recursive Case
    return arr[index] + array_sum(arr , index + 1)

# Example usage:
arr = [1, 2, 3, 4 , 5]
result = array_sum(arr, 0)
print("The sum of the array is:", result)