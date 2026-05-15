def find_duplicates(arr): 
    seen = set() 
    duplicates = set() 

    for num in arr: 
        if num in seen: 
            duplicates.add(num) 
        else: 
            seen.add(num) 

    return list(duplicates)

print(find_duplicates([1, 2, 3, 4, 2, 5, 1]))