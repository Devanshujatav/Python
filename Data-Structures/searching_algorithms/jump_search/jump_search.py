from cmath import sqrt
import math

def jump_search(arr , target): 
    n = len(arr) 
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
        
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
        
    return -1

# Example usage
if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = jump_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in array.")