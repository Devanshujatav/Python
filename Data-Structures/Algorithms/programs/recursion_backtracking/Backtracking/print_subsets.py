def print_subsets(arr):
    subset = []
    def backtrack(index):
        # Base Case:
        if index == len(arr):
            print(subset)
            return
        
        # Include the current element
        subset.append(arr[index])
        backtrack(index + 1)

        # Remove the last element
        subset.pop()

        # Exclude the current element
        backtrack(index+1)

    backtrack(0)


# Example usage:
arr = [1, 2, 3]
print_subsets(arr)