# Count Frequency of Elements

def count_frequency(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    return freq

print(count_frequency([1,2,2,3,3,4]))