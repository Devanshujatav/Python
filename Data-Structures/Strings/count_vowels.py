s = input("Enter a string: ")
vowels = []
count = 0

for char in s:
    if char.lower() in "aeiou":
        vowels.append(char)
        count += 1

vowels.sort()  # Sort the vowels alphabetically
#list(set(vowels))  # Remove duplicates from the list of vowels
print(f"The number of vowels in the string is : {count}")
print(f"The vowels in the string are: {', '.join(list(set(vowels)))}")