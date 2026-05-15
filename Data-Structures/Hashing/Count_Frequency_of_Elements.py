# Count Frequency of Elements

def count_frequency(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    return freq

print(count_frequency([1,2,2,3,3,4]))


#c    nums = list(map(int, input("Enter numbers separated by space: ").split()))
def count_frequency_manually(nums):
    freq = {}
    for x in nums:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    
    return freq


