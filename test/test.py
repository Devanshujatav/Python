def permutations(nums):

    result = []

    def backtrack(path):

        # Base Case
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:

            # Skip used numbers
            if num in path:
                continue

            # Choose
            path.append(num)

            # Explore
            backtrack(path)

            # Undo
            path.pop()

    backtrack([])

    return result


print(permutations([1, 2, 3]))