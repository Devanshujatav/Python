numbers = [10, 20, 30, 40]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print(smallest)